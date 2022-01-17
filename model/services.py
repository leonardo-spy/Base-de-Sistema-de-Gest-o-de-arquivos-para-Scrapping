#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.bancodedados import onlyCommit
import config
import pathlib
import pandas as pd
from os import remove

''' TODO: criar função que leva um sql que seja a diferença de do salvamento de cada consulta para conseguir criar uma função unica que utiliza desta diferença para salvar todos os serviços. '''

def verifyFolder(serviceId):
    serviceName = ''
    from controller.manageServices import processServices
    serviceName = processServices()[serviceId]
    pathlib.Path('./finalizados/'+str(serviceName)).mkdir(parents=True, exist_ok=True)
    return serviceName

def setServiceConsultaSimples(results,fileName,fileId):
    if config.LOCAL:
        serviceName = verifyFolder(0)
        planilha_resultado = pd.DataFrame(results)
        planilha_resultado.to_csv("./finalizados/"+serviceName+"/"+fileName+".csv",index = False,header =["Documento","Resultado"])
    else:
        planilha_resultado_tmp = pd.DataFrame(results)
        planilha_resultado_tmp.to_csv('./{}_tmp.csv'.format(fileName),index = False)
        pathCsv = str(pathlib.Path('./{}_tmp.csv'.format(fileName)).resolve())

        sql = 'DROP TEMPORARY TABLE IF EXISTS tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        sql = 'CREATE TEMPORARY TABLE tabela_temporaria_00 LIKE resultado_servico0;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao criar tabela temporaria!')
            return None
        
        sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE tabela_temporaria_00 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' ( @documento,@resultado ) SET documento = @documento,resultado = @resultado,arquivo = {};".format(pathCsv,fileId)
        result = onlyCommit(sql)
        if not result:
            print('Erro ao carregar o Csv na tabela temporaria!')
            return None
        
        sql = "INSERT INTO resultado_servico0 ( documento,resultado,arquivo) SELECT documento,resultado,arquivo from tabela_temporaria_00 WHERE  documento IS not NULL and documento!='' and documento REGEXP '^[0-9]+$';"
        result = onlyCommit(sql)
        if not result:
            print('Erro ao inserir da tabela temporaria para a principal!')
            return None
        
        sql = 'DROP TEMPORARY TABLE tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        remove(pathCsv)
    return True

def setServiceTeste2(results,fileName,fileId):
    if config.LOCAL:
        serviceName = verifyFolder(1)
        planilha_resultado = pd.DataFrame(results)
        planilha_resultado.to_csv("./finalizados/"+serviceName+"/"+fileName,index = False,header =["Documento","Resultado"])
    else:
        planilha_resultado_tmp = pd.DataFrame(results)
        planilha_resultado_tmp.to_csv('./{}_tmp.csv'.format(fileName),index = False)
        pathCsv = str(pathlib.Path('./{}_tmp.csv'.format(fileName)).resolve())

        sql = 'DROP TEMPORARY TABLE IF EXISTS tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        sql = 'CREATE TEMPORARY TABLE tabela_temporaria_00 LIKE resultado_servico1;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao criar tabela temporaria!')
            return None
        
        sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE tabela_temporaria_00 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' ( @documento,@resultado ) SET documento = @documento,resultado = @resultado,arquivo = {};".format(pathCsv,fileId)
        result = onlyCommit(sql)
        if not result:
            print('Erro ao carregar o Csv na tabela temporaria!')
            return None
        
        sql = "INSERT INTO resultado_servico1 ( documento,resultado,arquivo) SELECT documento,resultado,arquivo from tabela_temporaria_00 WHERE  documento IS not NULL and documento!='' and documento REGEXP '^[0-9]+$';"
        result = onlyCommit(sql)
        if not result:
            print('Erro ao inserir da tabela temporaria para a principal!')
            return None
        
        sql = 'DROP TEMPORARY TABLE tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        remove(pathCsv)
    return True

def setServiceTeste3(results,fileName,fileId):
    if config.LOCAL:
        serviceName = verifyFolder(2)
        planilha_resultado = pd.DataFrame(results)
        planilha_resultado.to_csv("./finalizados/"+serviceName+"/"+fileName,index = False,header =["Documento","Resultado"])
    else:
        planilha_resultado_tmp = pd.DataFrame(results)
        planilha_resultado_tmp.to_csv('./{}_tmp.csv'.format(fileName),index = False)
        pathCsv = str(pathlib.Path('./{}_tmp.csv'.format(fileName)).resolve())

        sql = 'DROP TEMPORARY TABLE IF EXISTS tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        sql = 'CREATE TEMPORARY TABLE tabela_temporaria_00 LIKE resultado_servico2;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao criar tabela temporaria!')
            return None
        
        sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE tabela_temporaria_00 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' ( @documento,@resultado ) SET documento = @documento,resultado = @resultado,arquivo = {};".format(pathCsv,fileId)
        result = onlyCommit(sql)
        if not result:
            print('Erro ao carregar o Csv na tabela temporaria!')
            return None
        
        sql = "INSERT INTO resultado_servico2 ( documento,resultado,arquivo) SELECT documento,resultado,arquivo from tabela_temporaria_00 WHERE  documento IS not NULL and documento!='' and documento REGEXP '^[0-9]+$';"
        result = onlyCommit(sql)
        if not result:
            print('Erro ao inserir da tabela temporaria para a principal!')
            return None
        
        sql = 'DROP TEMPORARY TABLE tabela_temporaria_00;'
        result = onlyCommit(sql)
        if not result:
            print('Erro ao deletar tabela temporaria!')
            return None
        
        remove(pathCsv)
    return True