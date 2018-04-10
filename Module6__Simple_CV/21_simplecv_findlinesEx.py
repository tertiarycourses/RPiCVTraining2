from SimpleCV import Image
import time

##img=Image('line.tiff')
##img.grayscale().findLines().show()
##time.sleep(5)
img=Image('lines.jpg')
lines=img.findLines()
lines.draw(width=3)
img.show()
time.sleep(5)
