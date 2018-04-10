from picamera import PiCamera
import time
from picamera import Color


camera = PiCamera()
camera.start_preview()
camera.annotate_text = "Hello world!"
camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
time.sleep(5)
camera.capture('test.jpg')
camera.stop_preview()
