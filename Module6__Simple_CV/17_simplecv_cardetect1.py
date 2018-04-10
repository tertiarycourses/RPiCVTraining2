from SimpleCV import Image
from SimpleCV import Color
import time

car_in_lot = Image("parking-car.png")
car_not_in_lot = Image("parking-no-car.png")


car = car_in_lot.crop(470,200,200,200)
car.show()
yellow_car = car.colorDistance(Color.YELLOW)
yellow_car.show()
only_car = car - yellow_car
#only_car.show()
print only_car.meanColor()

car_not_in_lot = Image("parking-no-car.png")
no_car = car_not_in_lot.crop(470,200,200,200)
yellow_car = no_car.colorDistance(Color.YELLOW)
#yellow_car.show()
only_car = car - yellow_car
print only_car.meanColor()




