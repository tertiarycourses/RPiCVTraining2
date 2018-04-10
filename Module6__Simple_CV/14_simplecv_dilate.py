from SimpleCV import Image
import time

lenna = Image("lena.png")
dilated = lenna.dilate(10)
d=dilated.show()
time.sleep(5)
d.quit()
