import cv2
import numpy as np

image = np.zeros((200,200,3))
cv2.line(image,(0,199),(199,0),(0,0,255),2)


while (True):

    cv2.imshow('Line',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
