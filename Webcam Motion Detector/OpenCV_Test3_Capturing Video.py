import cv2 
import time

video= cv2.VideoCapture(1)

check, frame= video.read()
time.sleep(1)

f_count= 0

while True:
     
     f_count= f_count + 1
     check, frame= video.read()
     print(check)
     print(frame)
     
     gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     #time.sleep(5)
     cv2.imshow('Capturing', gray)
     
     key= cv2.waitKey(1)
     if key==ord('e'):
          break

print(f_count)
video.release()
cv2.destroyAllWindows()