from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(5)
camera.capture('foo.jpg', resize=(320, 240))
camera.stop_preview()
