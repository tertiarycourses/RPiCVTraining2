from SimpleCV import Camera
import time

cam = Camera()

img = cam.getImage()
img.show()
time.sleep(5)
