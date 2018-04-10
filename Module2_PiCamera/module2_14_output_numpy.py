#python 3.0
##import time
##import picamera
##import numpy as np
##
##with picamera.PiCamera() as camera:
##    camera.resolution = (320, 240)
##    camera.framerate = 24
##    time.sleep(2)
##    output = np.empty((240, 320, 3),dtype=np.uint8)
##    camera.capture(output, 'rgb')


#http://picamera.readthedocs.io/en/release-1.12/recipes2.html
#python 2.7
import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.framerate = 24
    time.sleep(2)
    img = np.empty((112 * 128 * 3,), dtype=np.uint8)
    camera.capture(img, 'rgb')
    img = img.reshape((112, 128, 3))

    # img = img[:100, :100, :]
    print img
    
