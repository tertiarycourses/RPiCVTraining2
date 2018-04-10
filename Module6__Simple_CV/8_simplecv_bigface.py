from SimpleCV import Image
import time

lenna = Image("lena.png")
bigface = lenna.scale(3)
d=bigface.show()
time.sleep(5)
d.quit()
