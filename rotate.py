# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:23:19 2023

@author: afsal
"""

import cv2

#back and white 
img=cv2.imread('cv2.jpg',1)
resized=cv2.resize(img,(500,500),
                   interpolation=cv2.INTER_NEAREST)
image=cv2.rotate(resized,cv2.ROTATE_90_COUNTERCLOCKWISE)
sts=cv2.imwrite("ROTATE.jpg",resized)
cv2.imshow("view",image)
cv2.waitKey(0)
cv2.destroyallwindows()
