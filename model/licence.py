#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.bancodedados import fetchOne,fetchAll

def verifylicence(userid):
    sql = 'SELECT id,ativo,IF(data_expiracao >= NOW(),"1","0") as exp FROM cliente_licenca where id = {};'.format(int(userid))    
    result = fetchAll(sql)
    if not result:
        return None
    else:
        return result[0]
    pass

def verifymachine(infomachine):
    sql = 'SELECT idcliente FROM cliente_maquina WHERE uuid = {} LIMIT 1;'.format(infomachine)
    result = fetchOne(sql)
    if not result:
        return None
    else:
        return int(result[0])