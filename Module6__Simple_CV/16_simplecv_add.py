from SimpleCV import Image
import time

imgA = Image("simplecv.png")
img = imgA + imgA
img = imgA - imgA
img = imgA * imgA
img = imgA / imgA
d=img.show()
time.sleep(5)
d.quit()
