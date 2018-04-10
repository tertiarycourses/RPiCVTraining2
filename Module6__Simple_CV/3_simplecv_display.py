from SimpleCV import *
import time

cam = Camera()
disp = Display()

img = cam.getImage()
d=img.save(disp)
time.sleep(5)
#d.quit()


