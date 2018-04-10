
from SimpleCV import Image
import time

car_in_lot = Image("parking-car.png")
print "Height=", car_in_lot.height
print "Width=", car_in_lot.width
car = car_in_lot.crop(470,200,200,200)
d=car.show()
time.sleep(5)
d.quit()
