from SimpleCV import Image
import time

img=Image('lena.png')
img.grayscale().findLines().show()
time.sleep(5)
