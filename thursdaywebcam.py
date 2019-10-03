import cv2
import time
cap=cv2.VideoCapture('http://192.168.43.1:8080/video')
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('s'):
        a=time.time()
        cv2.imwrite(str(a)+'.jpg',frame)
