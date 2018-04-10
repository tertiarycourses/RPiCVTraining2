from SimpleCV import Image
import time

lenna = Image("lena.png")
inverted = lenna.invert()
d=inverted.show()
time.sleep(5)
d.quit()
