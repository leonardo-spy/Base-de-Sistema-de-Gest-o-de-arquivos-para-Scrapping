#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
#from main import HOST_DBB,USER_DBB,PASSWORD_DBB,DATABASE_DBB
import config
MYDB = None
def conexaoBanco():
    global MYDB
    if not MYDB or not MYDB.is_connected():
        MYDB = mysql.connector.connect(host=config.HOST_DBB, user=config.USER_DBB, passwd=config.PASSWORD_DBB, database=config.DATABASE_DBB,allow_local_infile=True)
    return MYDB