#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.file import anyFile
from model.bancodedados import fetchOne,fetchAll,onlyCommit
import config
import pathlib
import pandas as pd
from os import rename

def canWork(userid):
    if anyFile(userid):
        return True
    else:
        return False

def getFileCanWork(userid):
    fileId = serviceId = name = ''
    docs = {}
    print('Verificando se existe arquivos para ser trabalhado.')
    if config.LOCAL:
        from controller.manageServices import processServices
        for idservice,service in processServices().items():
            pathlib.Path('./arquivos/'+str(service)).mkdir(parents=True, exist_ok=True)
            for file in pathlib.Path('./arquivos/'+str(service)).iterdir():
                if file.suffix == '.csv':
                    serviceId = idservice
                    name = file.stem
                    documentos_csv = pd.read_csv("./arquivos/"+str(service)+"/"+file.name,header=None,usecols=[0])
                    docs = dict(enumerate(temp[0] for temp in documentos_csv.values))
                    break
                
            if serviceId != '':
                break
    else:
        sql = 'SELECT id,servico,nome FROM clientes_arquivos WHERE cliente = {} ORDER BY atuando asc LIMIT 1;'.format(int(userid))
        result = fetchOne(sql)
        if not result:
            return None
        else:
            fileId,serviceId,name = result[0],result[1],result[2]
        sql = 'SELECT id,documento FROM cliente_docs_em_processo WHERE arquivo = {} ORDER BY atuando asc LIMIT 400;'.format(int(fileId))
        result = fetchAll(sql)
        if not result:
            return None
        else:
            docs = result

    return [fileId,serviceId,name,docs]

def verifyFile(fileName,fileId):
    '''Verificar se os documentos do ja estão concluidos e finalizar o arquivo '''
    if config.LOCAL:
        pathlib.Path('./backup/').mkdir(parents=True, exist_ok=True)
        rename("./arquivos/{}.csv".format(fileName), "./backup/{}.csv".format(fileName))
    else:
        sql = "UPDATE clientes_arquivos SET `ativo` = 0 WHERE `id` = {};".format(fileId)
        result = onlyCommit(sql)
        if not result:
            print('Erro ao desativar o arquivo!')
            return None
    return True