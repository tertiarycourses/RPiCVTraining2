from SimpleCV import Image
import time

lenna = Image("lena.png")
warped = lenna.warp(((100,10),(300,10), (450,300), (10,300)))
d=warped.show()
time.sleep(5)
d.quit()
