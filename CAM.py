# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
i = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame',frame)
        cv2.waitKey(0)
        cv2.imwrite(str(i)+'.png',frame)
        print('capture image No.%d \n'%i)
        i += 1
        cv2.destroyWindow('frame')
        time.sleep(5)
    else:
        break

cap.release()
cv2.destroyAllWindows()
