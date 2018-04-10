from SimpleCV import *
import time
import matplotlib.pyplot as plt


#sudo apt-get install python-gi-cairo
img = Image('lena.png')
#img = Image('simplecv')
gray = img.toGray()
histogram = gray.histogram(255)
print len(histogram)
plt.plot(histogram, range(255))

plt.show()

#plt.savefig("hist.png")

 
