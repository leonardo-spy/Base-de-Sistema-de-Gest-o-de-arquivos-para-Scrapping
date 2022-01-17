#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.services import setServiceConsultaSimples,setServiceTeste2,setServiceTeste3
from controller.ManageFile import verifyFile
from servicesExtract import serviceConsultaSimples as ConsultaSimples,serviceTeste2 as Teste2,serviceTeste3 as Teste3

def process(userid,driver,file):
    results = []
    fileId,serviceId,name,docs = file[0],file[1],file[2],file[3]
    print('Iniciando processo no arquivo ({}) \"{}\" no serviço \'{}\' ({}) com {} documento(s).'.format(fileId,name,serviceId,processServices()[serviceId],len(docs)))
    for doc in docs:
        result = processServices(doc,serviceId,userid,driver)
        driver = result[0]
        results.append(result[1])


    saveResult(results,serviceId,name,fileId)

    verifyFile(name,fileId)

    return driver
    

def processServices(doc = None,service = None,userid = None,driver = None):
    
    services = {
        0: serviceConsultaSimples(doc,userid,driver) if service == 0 else 'Serviço de Consulta Simples',
        1: serviceTeste2(doc,userid,driver) if service == 1 else 'Serviço Teste 2',
        2: serviceTeste3(doc,userid,driver) if service == 2 else 'Serviço Teste 3',
    }
    ''' Retorno para conseguir os nomes dos serviços'''
    if doc == None and service == None and userid == None and driver == None:
        return services
        
    return services.get(service, "Opção inválida.")

def serviceConsultaSimples(doc,userid,driver):
    driver,result = ConsultaSimples.default(driver,doc)
    return driver,result

def serviceTeste2(doc,userid,driver):
    driver,result = Teste2.default(driver,doc)
    return driver,result

def serviceTeste3(doc,userid,driver):
    driver,result = Teste3.default(driver,doc)
    return driver,result

def saveResult(results,serviceId,fileName,fileId):
    ''' método antigo: 0: (setServiceConsultaSimples(result.doc) for result in results) if serviceId == 0 else 'Resultado do Serviço de Consulta Simples','''
    services = { 
        0: setServiceConsultaSimples(results,fileName,fileId) if serviceId == 0 else 'Resultado do Serviço de Consulta Simples',
        1: setServiceTeste2(results,fileName,fileId) if serviceId == 1 else 'Resultado do Serviço Teste 2',
        2: setServiceTeste3(results,fileName,fileId) if serviceId == 2 else 'Resultado do Serviço Teste 3',
    }
    return services.get(serviceId, "Opção inválida.")
