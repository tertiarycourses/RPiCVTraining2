from SimpleCV import Image
from SimpleCV import Camera
import time

cam = Camera()
img = cam.getImage()
imgBin=img.binarize()
blobs=imgBin.findBlobs()
d=blobs.show(width=5)
time.sleep(5)
d.quit()
