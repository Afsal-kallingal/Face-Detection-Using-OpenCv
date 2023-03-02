# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:36:21 2023

@author: afsal
"""

import cv2

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture the frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was properly captured
    if not ret:
        break

    # Write the frame to the VideoWriter object
    out.write(frame)

    # Show the frame in a window
    cv2.imshow('Webcam Video', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter and VideoCapture objects
out.release()
cap.release()

# Close all the windows
cv2.destroyAllWindows()