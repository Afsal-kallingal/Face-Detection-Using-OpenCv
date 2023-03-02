# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:02:52 2023

@author: afsal
"""

import cv2
cam=cv2.VideoCapture("http://192.168.43.1:4747/video")
while True:
    check,frame=cam.read()
    cv2.imshow("video",frame)
    key=cv2.waitKey(1)
    if key==27:
        break   
cam.release()
cv2.destroyAllWindows    
        