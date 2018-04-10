from SimpleCV import Image
import time

lenna = Image("lena.png")
rotated = lenna.rotate(90)
d=rotated.show()
time.sleep(5)
d.quit()
