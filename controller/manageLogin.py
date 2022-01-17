#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from controller.manageDriver import goToStart,goToLogin
from controller.guru import resolveCaptchaImg
from model.login import getSenha


def processLogin(userId,driver):
    '''TODO:verificarlogado()'''
    login = getSenha(userId)
    if not login:
        return driver,False
    driver = goToStart(driver)
    driver = goToLogin(driver)
    captcha = getCaptcha(driver)
    captchaText = resolveCaptchaImg(captcha)
    driver = setLogin(login[0],login[1],captchaText,driver)
    return driver,True



def getCaptcha(driver):
    while True:        
        element = driver.find_element_by_xpath("/Image[@Value.Value='https://CENSURADO/captcha']")
        if element:
            return element.get_attribute('src')
        sleep(0.2)

def setLogin(username,password,captcha,driver):
    return driver
