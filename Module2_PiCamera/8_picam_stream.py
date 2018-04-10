##from io import BytesIO
##from picamera import PiCamera
##
##stream = BytesIO()
##camera = PiCamera()
##camera.resolution = (640, 480)
##camera.start_recording(stream, format='h264', quality=23)
##camera.wait_recording(5)
##camera.stop_recording()
##print stream.array.shape

#--------------------------------------------------
import time
import picamera
import picamera.array

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        #print stream.array.shape
        camera.resolution = (100, 100)
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, 'rgb')
        # Show size of RGB data
        print stream.array.shape
        camera.stop_preview()
        print stream.array[1][1]
