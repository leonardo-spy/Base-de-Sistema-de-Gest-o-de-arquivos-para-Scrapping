#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  sys import argv
from time import sleep
import threading
import requests
from subprocess import check_output
from uuid import getnode#,UUID
from main import get_Threads
import config
from controller.manageDriver import verifywindriver,closewindriver,startApp
from controller.manageLogin import processLogin
from controller.ManageFile import getFileCanWork
from controller.manageServices import process
from model.licence import verifymachine,verifylicence

'''Variavel que armazena o estado da conexao internet'''
'''INTERNET = False'''

'''
    Funçao que é inicializada com o inicio da aplicação para instânciar toda a macro.
    @return ? Bolean: apenas representa se a função foi terminada de forma saúdavel ou não.
'''


def initialize():
    #global PROGRAM_PATH
    global INTERNET
    '''Argumento opcional que muda o local do programa alvo padrão'''
    if len(argv) > 1:
       config.PROGRAM_PATH = argv[1]

    print('Verificando Acesso a Internet...')
    INTERNET = False

    '''Inicializa a thread que verifica conexao com internet'''
    get_Threads().append(threading.Thread(target=internet,name="internet"))
    get_Threads()[len(get_Threads())-1].start()
    while not INTERNET:
        print('sem acesso a internet...')
        sleep(0.20)

    print('Verificando Banco de dados...')
    userid = verifymachine(infomachine())

    if not userid:
        print('Máquina Invalida:{}'.format(str(infomachine())))
        return shutdownThreads(False)
    licenseUser = verifylicence(userid)
    if not licenseUser:
        print('Licença Invalida')
        return shutdownThreads(False)
    elif str(licenseUser[0]) != str(userid):
        print('Erro ao consultar usuario, encerrando...')
        return shutdownThreads(False)
    elif str(licenseUser[1]) == "0":
        print('Usuario não está ativo, encerrando...')
        return shutdownThreads(False)
    elif str(licenseUser[2]) == "0":
        print('Usuario expirado, encerrando...')
        return shutdownThreads(False)
    
    if not work(userid):
        return shutdownThreads(False)

    return shutdownThreads(True)

def work(userid):
    skip = False
    file = None
    while True:
        try:
            if INTERNET:
                if not skip:
                    file = getFileCanWork(userid)
                if skip or file:                    
                    if not skip:
                        verifywindriver()                        
                        #driver = startApp()
                        #driver,result = processLogin(userid,driver)
                        result = True
                        driver = None
                        if not result:
                            driver.close()
                            closewindriver()
                            return False
                    skip = False
                    driver = process(userid,driver,file)
                    file = getFileCanWork(userid)
                    if file:
                        skip = True
                    else:
                        driver.close()
                        closewindriver()
                        break
                else:
                    sleep(10)
                #break
            sleep(5)
        except:
            return False
    return True

'''
    Funçao que pega informações da máquina
    @return machineInfo String: string que armazena o id da máquina que foi gerado pelo algoritmo.
'''


def infomachine():
    #machineInfo = check_output('wmic csproduct get UUID')    
    #machineInfo = UUID(int=getnode())
    machineInfo = getnode()
    return machineInfo


'''
    Funçao que verifica se tem internet
    @params : Todos os parametros sao padrões para checagem
'''


def internet(url="https://www.google.com.br/", timeout=5):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    TIME_DELAY = 2

    global INTERNET

    while True:
        try:
            requests.get(url=url, timeout=timeout)
            INTERNET = True
        except:
            INTERNET = False
            pass

        if getattr(threading.currentThread(), "stop", False):
            break

        sleep(TIME_DELAY)

def shutdownThreads(return_tmp = None):
    #global THREADS
    for thread in get_Threads():
        thread.stop = True
    if return_tmp == None:
        pass
    else:
        return return_tmp