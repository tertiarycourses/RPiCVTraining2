from picamera import PiCamera

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_recording('1.h264')
camera.wait_recording(5)
for i in range(2, 5):
    camera.split_recording('%d.h264' % i)
    camera.wait_recording(5)
    print ('record %d.h264' % i)
camera.stop_recording()
print "Complete All"
