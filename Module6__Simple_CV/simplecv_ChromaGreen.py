from SimpleCV import *

sleep_time = 2 #the amount of time to show each image for

#Load and show the greenscreen image
print "Showing Greenscreen image"
greenscreen = Image("green-screen-person.jpg")
greenscreen.show()
time.sleep(sleep_time)


#load and show the background image
print "Showing background image"
background = Image("green-screen-wallst.jpg")
background.show()
time.sleep(sleep_time)

#Create the mask to apply and show the mask
print "Showing Masked Image"
mask = greenscreen.hueDistance(color=Color.GREEN).binarize()
mask.show()
time.sleep(sleep_time)

#Combine the mask and other images to get the final result
print "Showing final image"
result = (greenscreen - mask) + (background - mask.invert())
result.show()
time.sleep(sleep_time)
