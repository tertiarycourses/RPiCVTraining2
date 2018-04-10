from SimpleCV import Camera, Display
cam=Camera()
WeightFactor=0.8
t0=cam.getImage()
disp=Display((t0.size()))

while not disp.isDone():
    t1=cam.getImage()
    img= (t1*WeightFactor)+(t0*(1-WeightFactor))
    img.save(disp)
    t0=t1
