from SimpleCV import *
import time


frame = Image("lena.png")

# Look for a face
facedetect = frame.findHaarFeatures('facetrack-training.xml')
matches=0
if facedetect:
    facedetect.draw()
    frame.show()
    for f in facedetect:
        matches += 1
print "match=",matches    

