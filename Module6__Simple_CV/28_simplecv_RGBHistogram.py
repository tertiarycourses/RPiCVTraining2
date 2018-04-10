from SimpleCV import Image
import time
import matplotlib.pyplot as plt


img = Image('lena.png')
#img = Image('simplecv')
(red, green, blue) = img.splitChannels(False)
imgr = red.histogram(255)
imgg = green.histogram(255)
imgb = blue.histogram(255)

plt.plot(imgr)
plt.plot(imgg)
plt.plot(imgb)
plt.show()
#plt.savefig("histrgb.png")
