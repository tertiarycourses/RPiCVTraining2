from SimpleCV import Image
import time

lenna = Image("lena.png")
print "Height=", lenna.height
print "Width=", lenna.width
face = lenna.crop(200,200,200,200)
d=face.show()
time.sleep(5)
d.quit()
