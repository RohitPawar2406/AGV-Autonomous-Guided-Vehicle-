#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:57:10 2021

@author: rohit
"""
import base64
import numpy as np
import cv2
import requests
import requests
'''url = 'http://localhost:3000/'
#url = 'https://httpbin.org/post'
payload = {'name':"Rohit",'surname':'Pawar'}
res = 'ROHIT_PAWAR_7058508482'
r = requests.post(url,json=payload)
print(r)
print(dir(r))'''

img = cv2.imread('1.jpeg')
im_arr = cv2.imencode('.jpeg', img)  # im_arr: image in Numpy one-dim array format.
im_bytes = im_arr[1].tobytes()
im_b64 = base64.b64encode(im_bytes)
print(type(im_b64))

im_b64_to_String = im_b64.decode('UTF-8')
print(type(im_b64_to_String))
print(im_b64_to_String==im_b64)

obj1 = {"name":im_b64_to_String}
print(type(obj1['name']))
req = requests.post('http://localhost:3000/', json=obj1)
print(req)
print(im_bytes==im_b64_to_String)