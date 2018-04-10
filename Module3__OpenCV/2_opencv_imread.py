import cv2

img = cv2.imread('lena.png',1)
cv2.imshow('Lena',img)
cv2.waitKey(5000)
