#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import config

def resolveCaptchaImg(img_bytes):    
    files = {'file': img_bytes}
    data = {'key': config.KEY_GURU, 'method': 'post'}
    r = requests.post('http://api.captcha.guru/in.php', files=files, data=data)
    if r.ok and r.text.find('OK') > -1:
        reqid = r.text[r.text.find('|')+1:]
        for timeout in range(40):
            r = requests.get('http://api.captcha.guru/res.php?key='+config.KEY_GURU+'&action=get&id='+reqid)
            if r.text.find('CAPCHA_NOT_READY') > -1:
                time.sleep(3)
            if r.text.find('ERROR') > -1:
                print (r.text)
                return ''
            if r.text.find('OK') > -1:
                return r.text[r.text.find('|')+1:]
    return ''