import cv2
img = cv2.imread('lena.png',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
##sobel = cv2.Sobel(img)
##scharr = cv2.Scharr(img)

while (True):

    cv2.imshow('laplacian',laplacian)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
