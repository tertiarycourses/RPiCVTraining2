from SimpleCV import Image
import time

lenna = Image("lena.png")
grey = lenna.grayscale()
d=grey.show()
time.sleep(5)
d.quit()
