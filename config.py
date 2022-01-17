#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import sys
import platform

def initialize():
    global HOST_DBB,USER_DBB,PASSWORD_DBB,DATABASE_DBB,KEY_GURU,PROGRAM_PATH,LOCAL,OS_PLATAFORM,OS_VERSION,IS_EXE
    OS_PLATAFORM = sys.platform
    OS_VERSION =(platform.machine().endswith('64') == True)
    if getattr(sys, 'frozen', False):        
        IS_EXE = True
    else:
        IS_EXE = False

    config = configparser.RawConfigParser()
    config.read('config')
    sections = config.sections()    
    if not sections or not 'CLIENTE' in sections:
        HOST_DBB = '127.0.0.1'
        USER_DBB = 'root'
        PASSWORD_DBB = ''
        DATABASE_DBB = 'temp'
        KEY_GURU = ''
        PROGRAM_PATH = r""
        LOCAL=False
        print('Inicializando com váriaveis padrão...')
    else:
        details_dict = dict(config.items('CLIENTE'))
        HOST_DBB=details_dict['host_dbb']
        USER_DBB=details_dict['user_dbb']
        PASSWORD_DBB=details_dict['password_dbb']
        DATABASE_DBB=details_dict['database_dbb']
        KEY_GURU=details_dict['key_guru']
        PROGRAM_PATH=details_dict['program_path']
        LOCAL=details_dict['local']== 'True'
        print('Arquivo de configuração carregado...')