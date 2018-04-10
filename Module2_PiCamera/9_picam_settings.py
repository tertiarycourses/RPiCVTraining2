from picamera import PiCamera
import time

camera = PiCamera(resolution=(1280, 720), framerate=30)
camera.framerate = 30
camera.brightness = 70

camera.shutter_speed = 6000000
camera.iso = 30

camera.start_preview()
time.sleep(10)
camera.capture('testA.jpg')
camera.stop_preview()
