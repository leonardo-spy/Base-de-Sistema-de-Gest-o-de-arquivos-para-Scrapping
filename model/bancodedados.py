#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.ManageDatabase import conexaoBanco

def onlyCommit(sql):
    mydb = conexaoBanco()
    try:
        mycursor = mydb.cursor()
    except Exception as e:
        print(e)
        return False
    try:
        mycursor.execute(sql)
        mydb.commit()
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
        return True
    except Exception as e:
        print(e)
        try:
            mydb.rollback()
        except Exception as rollerror:
            print(str(rollerror))        
        try:
            if(mydb.is_connected()):
                mycursor.close()
                mydb.close()
        except Exception as expp:
            print(str(expp))  
        return False

def fetchOne(sql):
    mydb = conexaoBanco()
    try:
        mycursor = mydb.cursor()
    except Exception as e:
        print(e)
        return False
    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
        return myresult
    except Exception as e:
        print(e)
        try:
            mydb.rollback()
        except Exception as rollerror:
            print(str(rollerror))        
        try:
            if(mydb.is_connected()):
                mycursor.close()
                mydb.close()
        except Exception as expp:
            print(str(expp))  
        return ''

def fetchAll(sql):
    mydb = conexaoBanco()
    try:
        mycursor = mydb.cursor()
    except Exception as e:
        print(e)
        return False
    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
        return myresult
    except Exception as e:
        print(e)
        try:
            mydb.rollback()
        except Exception as rollerror:
            print(str(rollerror))        
        try:
            if(mydb.is_connected()):
                mycursor.close()
                mydb.close()
        except Exception as expp:
            print(str(expp))  
        return ''
