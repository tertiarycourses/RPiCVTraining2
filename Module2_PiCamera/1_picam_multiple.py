from picamera import PiCamera
import time

camera = PiCamera()
camera.start_preview()
time.sleep(10)
camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
camera.stop_preview()
