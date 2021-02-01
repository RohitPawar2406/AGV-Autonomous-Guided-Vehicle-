#!/usr/bin/env python
# coding: utf-8

# In[1]:

import base64
import numpy as np
import cv2
print("IHfsjd")


# In[2]:


import urllib.request
#url='https://obscure-cliffs-43212.herokuapp.com/pythontoExpress'
url = 'http://localhost:3000/'
headers={}
headers['temp']='1000'
headers['barcode']='000000'

img = cv2.imread('1.jpeg')
im_arr = cv2.imencode('.jpeg', img)  # im_arr: image in Numpy one-dim array format.
im_bytes = im_arr[1].tobytes()
im_b64 = base64.b64encode(im_bytes)
headers['base64'] = im_b64
 
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req=urllib.request.Request(url, headers=headers,data=im_b64)
resp=urllib.request.urlopen(req)
data=resp.read()
print("END")


# In[ ]:




