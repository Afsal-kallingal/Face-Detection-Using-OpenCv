# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:41:19 2023

@author: afsal
"""

import cv2
cap= cv2.VideoCapture(0)


check, img=cap.read()
    

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print('number of faces ',len(faces))
   

# Draw a rectangle around each face detected
for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Face Detection', img)    

# Display the resulting image

cv2.waitKey(0)
cv2.destroyAllWindows()
