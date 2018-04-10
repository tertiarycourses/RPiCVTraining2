
from SimpleCV import *
import time

matches = 0
try:
    cam = SimpleCV.Camera(0)
except:
    print "Can't open webcam"
    sys.exit()

while True:
    try:
        frame = cam.getImage()
    except:
        print "Can't grab frame from webcam"
        sys.exit()

    # Look for a face
    facedetect = frame.findHaarFeatures('facetrack-training.xml')

    if facedetect:
        facedetect.draw()
        frame.show()
        for f in facedetect:
            matches += 1
    print "match=",matches    
    time.sleep(1)
