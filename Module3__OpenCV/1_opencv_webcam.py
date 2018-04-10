import cv2

cam = cv2.VideoCapture(0)
ret, image = cam.read()
if ret:  
    cv2.imshow('Test',image)
    cv2.waitKey(0)
    cv2.imwrite('test.jpg',image)
cam.release()
