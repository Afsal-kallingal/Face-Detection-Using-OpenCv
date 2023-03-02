# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:58:14 2023

@author: afsal
"""

import cv2
cam=cv2.VideoCapture(0)
while True:
    check,frame=cam.read()
    e=0
    for i in range(0,10):
        e=e+i
        c=str(i)
        cv2.imwrite('i/'+c+'.jpg',frame)
        cv2.imshow('video',frame)
        
        if (e==10):
            cam.release()
            cv2.destroyAllWindows 
            
          
