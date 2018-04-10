from SimpleCV import Image
import time

car = Image("parking-car.png")
nocar = Image("parking-no-car.png")
img = car - nocar
d=img.show()
time.sleep(15)
d.quit()
