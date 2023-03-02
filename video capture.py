# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:36:08 2023

@author: afsal
"""

import cv2
cam=cv2.VideoCapture(0)
while True:
    check,frame=cam.read()
    cv2.imshow('video',frame)
    for i in range(0,10):
        c=str(i)
        cv2.imwrite('image/'+c+'.jpg',frame)
        
    key=cv2.waitKey(1)
    if key==27:
        break   
cam.release()
cv2.destroyAllWindows 