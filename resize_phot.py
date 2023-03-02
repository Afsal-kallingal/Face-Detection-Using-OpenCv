# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:51:36 2023

@author: afsal
"""

import cv2

#back and white 
img=cv2.imread('cv2.jpg',1)
print(img.shape)
resized=cv2.resize(img,(500,500),
                   interpolation=cv2.INTER_NEAREST)
print(resized.shape)
cv2.imshow("view",img)
cv2.waitKey(0)
cv2.destroyallwindows()
