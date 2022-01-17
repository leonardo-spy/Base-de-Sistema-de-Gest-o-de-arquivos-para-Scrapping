#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.bancodedados import fetchOne

def getSenha(userId):
    sql = 'SELECT `username`,`password` FROM `clientes_senha` where `cliente` = {} limit 1;'.format(int(userId))
    result = fetchOne(sql)
    if not result:
        return None
    else:
        return result[0],result[1]