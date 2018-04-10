import cv2
import numpy as np

image = np.zeros((200,200,3))
cv2.circle(image,(100,100),50,(0,255,0),-1)

while (True):

    cv2.imshow('Circle',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
