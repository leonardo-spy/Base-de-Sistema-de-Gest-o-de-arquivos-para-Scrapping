#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import check_output,Popen,CREATE_NEW_CONSOLE,PIPE,STDOUT
import config
from time import sleep
from appium import webdriver

def verifywindriver():
    pidarray = check_output('tasklist /fi "Imagename eq WinAppDriver.exe"').split()
    if len(pidarray)> 9 and pidarray[16] == b'WinAppDriver.exe':
        print('WinDriver já está em execução!')
    else:
        print('Inicializando WinDriver')
        while True:
            if config.OS_VERSION:
                Popen(r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe", shell=True,creationflags=CREATE_NEW_CONSOLE,stdout=PIPE,stderr=STDOUT)
            else:
                Popen(r"C:\Program Files\Windows Application Driver\WinAppDriver.exe", shell=True,creationflags=CREATE_NEW_CONSOLE,stdout=PIPE,stderr=STDOUT)
            pidarray = check_output('tasklist /fi "Imagename eq WinAppDriver.exe"').split()
            if len(pidarray)> 9 and pidarray[16] == b'WinAppDriver.exe':
                break
            else:
                if config.OS_VERSION:
                    Popen(r"C:\Program Files\Windows Application Driver\WinAppDriver.exe", shell=True,creationflags=CREATE_NEW_CONSOLE,stdout=PIPE,stderr=STDOUT)
                    pidarray = check_output('tasklist /fi "Imagename eq WinAppDriver.exe"').split()
                    if len(pidarray)> 9 and pidarray[16] == b'WinAppDriver.exe':
                        break
                sleep(0.20)
        print('WinDriver agora está em execução!')

def closewindriver():
    pidarray = check_output('TASKKILL /IM "WinAppDriver.exe" /T /F').split()
    if len(pidarray)> 12 and pidarray[12] == b'finalizado.':
        print('WinDriver Finalizado!')
    else:
        print('Erro ao finalizar WinDriver.')

def startApp():
    desired_caps = {}
    desired_caps["app"]=config.PROGRAM_PATH
    desired_caps["plataformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    driver = webdriver.Remote("http://127.0.0.1:4723",desired_caps)
    return driver

def goToStart(driver):
    while True:        
        driver.find_element_by_name("CENSURADO").click()
        if driver.find_element_by_name("CENSURADO"):
            return driver
        sleep(0.2)

def goToLogin(driver):
    while True:        
        driver.find_element_by_name("CENSURADO").click()
        if driver.find_element_by_name("CENSURADO"):
            return driver
        sleep(0.2)

