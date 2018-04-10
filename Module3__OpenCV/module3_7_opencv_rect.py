import cv2
import numpy as np

image = np.zeros((200,200,3))
cv2.rectangle(image,(20,20),(60,60),(255,0,0),1)


while (True):

    cv2.imshow('Rectangle',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
