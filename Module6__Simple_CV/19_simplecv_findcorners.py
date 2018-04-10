from SimpleCV import Image
import time
img=Image('lena.png')
img.grayscale().findCorners().show()
time.sleep(5)
#d.quit()
