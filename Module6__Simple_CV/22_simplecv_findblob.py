from SimpleCV import Image
import time

img=Image('blob.jpg')
#img=Image('lena.png')
imgBin=img.binarize()
blobs=imgBin.findBlobs()
d=blobs.show(width=5)
time.sleep(5)
d.quit()
