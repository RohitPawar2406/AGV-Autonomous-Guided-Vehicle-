#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:19:37 2021

@author: rohit
"""

print("Inside rohit.py")
# import the opencv library 
import cv2 
import base64
import requests
import json
import datetime
#import numpy as np  
  

# define a video capture object 
vid = cv2.VideoCapture(0) 

url = 'http://localhost:3000/'               # localhost of Nodejs script.
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame)
    
    im_arr = cv2.imencode('.jpeg', frame)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr[1].tobytes()         # Conversion off array in Raw Bytes
    im_b64 = base64.b64encode(im_bytes)    # Raw Bytes convereted into Base64 Bytes
    
    im_b64_to_String = im_b64.decode('UTF-8')   #Base64 Bytes to Base 64 String.
    
    data={"Image":im_b64_to_String}             # Base64 string saved in a dictionary. 
    r = requests.post(url,json=data)            # posting data to nodejs port
    print("Frame Send!!!")
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'):       # pressing 'q' to exit the frame and while loop breaks.
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()

