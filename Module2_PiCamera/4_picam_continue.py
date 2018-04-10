from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview()
time.sleep(2)

try:
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print 'Captured %s' % filename 
        time.sleep(30)
except (KeyboardInterrupt, SystemExit):
    camera.stop_preview()
    print "program exit"


#Stop the capturing by CTRL C
