
import cv2
import numpy as np

image = np.zeros((200,200,3))
cv2.ellipse(image,(99,99),(40,20),0,0,360,(128,128,128),-1)
cv2.imshow('Ellipse',image)
while (True):

    cv2.imshow('Ellipse',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
