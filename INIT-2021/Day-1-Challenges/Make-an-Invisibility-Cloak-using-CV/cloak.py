import cv
import numpy as np

video = cv.VideoCapture(0)

background=0

for i in range(30):
    ret,background=video.read()

background=np.flip(background, axis=1m)



while True:
    ret,img=video.read()
    img=np.flip(img, axis=1)
    hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blur=cv.GaussianBlur(hsv, (35,35), 0)
    cv.imshow("Display", img)

    lower=np.array([0,120,70])
    upper=np.array([10,255,255])
    mask01=cv.inRange(hsv, lower, upper)

    cv.imshow("Background", background)
    cv.imshow("mask01", mask01)
    k=cv.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv.destroyAllWindows()