from picamera import PiCamera
import datetime as dt

camera = PiCamera()
camera.start_recording('timestamped.h264')
start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < 10:
    camera.annotate_text =   dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(0.2)
camera.stop_recording()
print "complete"
