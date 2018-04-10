from picamera import PiCamera
import time

camera = PiCamera()
camera.start_preview()
time.sleep(2)
camera.capture_sequence([
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        ])
camera.stop_preview()

camera = PiCamera()
camera.start_preview()
time.sleep(10)
camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
camera.stop_preview()

