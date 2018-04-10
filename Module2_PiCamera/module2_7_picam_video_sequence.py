from picamera import PiCamera

camera = PiCamera()

camera.resolution = (640, 480)

for filename in camera.record_sequence([
            'clip01.h264',
            'clip02.h264',
            'clip03.h264']):
            print('Recording to %s' % filename)
            camera.wait_recording(10)



#oxmplayer my_video.h264
