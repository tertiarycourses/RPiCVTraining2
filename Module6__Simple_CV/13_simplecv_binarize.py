from SimpleCV import Image
import time

lenna = Image("lena.png")
binarize = lenna.binarize()
#binarize = lenna.binarize(127)
d=binarize.show()
time.sleep(5)
d.quit()
