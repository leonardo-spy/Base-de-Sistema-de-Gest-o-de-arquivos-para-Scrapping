#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.bancodedados import fetchOne

def anyFile(userid):
    sql = '{}'.format()
    if int(fetchOne(sql)) >= 1:
        return True
    else:
        return False