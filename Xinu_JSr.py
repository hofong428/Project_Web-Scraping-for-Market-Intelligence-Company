#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Xinu_JSr.py
@Time    :   2023/02/18 20:38:33
@Author  :   Codebat
@Version :   1.0
@Contact :   hofong.chang@gmail.com
'''



import requests
import execjs



jscode = open('./Xinu_params.js', 'r', encoding='utf-8').read()
parames = execjs.compile(jscode).call('main123')
print(parames)

# 加密参数逆向
json_data = {
    'payload':parames['payload'],
    'sig':parames['sig'],
    'v':1,
}
