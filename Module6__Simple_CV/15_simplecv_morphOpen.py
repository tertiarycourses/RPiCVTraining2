from SimpleCV import Image
import time

lenna = Image("lena.png")
##open = lenna.morphOpen()
##open.show()
##time.sleep(5)
closed = lenna.morphClose()
d=closed.show()
time.sleep(5)
d.quit()
