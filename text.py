# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:51:34 2023

@author: afsal

"""
#PUT TEXT

import cv2
image=cv2.imread('cv2.jpg',1)
position=(800,300)
cv2.putText(
    image,
    'SULU',
    position,
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,255,255),
    3)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyallwindows()