from picamera import PiCamera
import time
camera = PiCamera()
camera.image_effect = 'emboss'
camera.start_preview()
time.sleep(10)
camera.capture('test.jpg')
camera.stop_preview()
print "complete"
