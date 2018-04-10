from picamera import PiCamera

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(20)
camera.stop_recording()
print "Complete recording"

#oxmplayer my_video.h264
