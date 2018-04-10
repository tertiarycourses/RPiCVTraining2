import cv2
img1 = cv2.imread('lena.png',1)
img2 = cv2.imread('monkey.png',1)

##img1 = cv2.imread('ml.png')
##img2 = cv2.imread('opencv-logo.png')
##dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
##cv2.imshow('dst',dst)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


alpha=0.5
beta=0.5
gamma=1 
Output = (alpha*img1)+(beta*img2)+gamma
dis=cv2.addWeighted(img1,alpha,img2,beta,0)

while (True):

    cv2.imshow('dis',dis)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
