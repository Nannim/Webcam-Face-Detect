import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    #capture frame by frame
    ret, img = cap.read()
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('test', img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
cap.release()