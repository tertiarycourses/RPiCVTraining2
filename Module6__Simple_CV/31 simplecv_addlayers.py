from SimpleCV import *
import time

##lenna = Image('lena.png')
##facelayer = DrawingLayer((lenna.width, lenna.height))
##facebox = facelayer.centeredRectangle(center_point, facebox_dim)
##lenna.addDrawingLayer(facelayer)
##lenna.applyLayers()
##lenna.show()

lenna = Image('lena.png')
facelayer = DrawingLayer((lenna.width, lenna.height))
facebox_dim = (200,200)
center_point = (lenna.width / 2, lenna.height / 2)
facebox = facelayer.centeredRectangle(center_point, facebox_dim)
lenna.addDrawingLayer(facelayer)
lenna.applyLayers()
lenna.show()
time.sleep(1)
