import cv2
img1 = cv2.imread('lena.png',1)
img2 = cv2.imread('monkey.png',1)

#cv2.imshow('Addition',cv2.add(img1,img2))
##cv2.imshow('Minus1,cv2.subtract(img1,img2))
##cv2.imshow('Minus2',cv2.subtract(img2,img1))
while (True):
    cv2.imshow('Addition',cv2.add(img1,img2))
    k = cv2.waitKey(1) & 0xFF
    if k == ord('a'):
        break

cv2.destroyAllWindows()
cv2.waitKey(-1)

print "program exit"
