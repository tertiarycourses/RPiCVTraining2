from picamera import PiCamera
import time
camera = PiCamera()
camera.awb_mode = 'horizon'
camera.start_preview()
time.sleep(10)
camera.capture('test.jpg')
camera.stop_preview()
print "complete"
