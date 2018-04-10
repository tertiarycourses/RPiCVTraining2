##import cv2
##import matplotlib.pyplot as plt
##
##img = cv2.imread('lena.png',1)
##img = cv2.cvtColor ( img , cv2.COLOR_BGR2RGB )
##
##plt.imshow ( img ) , plt.title ('COLOR IMAGE'),
##plt.xticks([]) , plt.yticks([])
##plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr_img = cv2.imread('san_francisco.jpg')
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('san_francisco_grayscale.jpg',gray_img)

plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.xticks([])
plt.yticks([])
# to hide tick values on X and Y axis
plt.show()

##while True:
##    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
##    if k == 27: break            # Code for the ESC key
##
##cv2.destroyAllWindows()
