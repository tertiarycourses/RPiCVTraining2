import cv2

img = cv2.imread('lena.png',1)
input = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

output = cv2.GaussianBlur(input,(15,15),0)
##output = cv2.bilateralFilter(input,19,75,75)
##ouput = cv2.medianBlur(output,3)
#output=cv2.boxFilter(input,-1,(3,3),normalize=True)
while (True):

    cv2.imshow('output',output)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
