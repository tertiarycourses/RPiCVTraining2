from SimpleCV import Image
from SimpleCV import Color
import time

##candidate = Image('mypy.png')
##lake = Image('lake.png')
##mask=candidate.hueDistance(color=Color.GREEN).binarize()
##output=(lake - mask.invert()) + (candidate-mask)
##output.save('result.png')
##print "Complete"

##candidate = Image('mypy.png')
##lake = Image('lake.png')
##mask=candidate.hueDistance(color=Color.GREEN, minvalue = 40).binarize()
##output=(lake - mask.invert()) + (candidate-mask)
##output.save('result.png')
##print "Complete"


from SimpleCV import *
import time

print 'Displaying Candidate Image'
candidate = Image ('mypy.png')
candidate.show()
time.sleep(7)

print 'Displaying Background Image'
lake = Image ('lake.png')
lake.show()
time.sleep(7)

print 'Apply and display mask'
mask=candidate.hueDistance(color=Color.GREEN).binarize()
mask.show()
time.sleep(7)

print 'Chroma Key Effect'
output=(lake - mask.invert()) + (candidate-mask)
output.show()
time.sleep(7)
