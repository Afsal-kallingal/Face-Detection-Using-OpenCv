# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:39:41 2023

@author: afsal
"""

import cv2

#back and white 
img=cv2.imread('cv2.jpg',1)
cv2.imshow("view",img)
cv2.waitKey(0)
cv2.destroyallwindows()