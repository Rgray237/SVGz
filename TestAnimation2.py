import gizeh as gz
import numpy as np
import moviepy.editor as mpy
from SVGz import SVGz, SVGzAnimation
from SVGzFrame import *
from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as plt



def clip1():
    DURATION = 2.416666




    def make_frame(t):

        img = frame.getPILImage()
        img1 = frame.applyFilterToPILImg(img)
        arr = frame.PILToNumpy(img1)
        #arr = antialias(arr)
        return arr[:,:,:3]

    clip = mpy.VideoClip(make_frame, duration=DURATION)
    return clip

MyAnimator = SVGz()
animation = SVGzAnimation()
frame = SVGzFrame()
frame2 = SVGzFrame()
x = 0
y = 0
x2 = 120
y2 = 312
nd1 = SVGzLine(x,y,x2,y2)
nd2 = SVGzLine(x+60,y+178,x2+90,y2+532)
nd3 = SVGzLine(50,90,x2+40,y2+50)
nd4 = SVGzLine(x+10,y+20,x2,y2)
line1 = SVGzLine(0,0,10,50)
line2 = SVGzLine(10,20,40,100)
line3 = SVGzLine(300,23,95,1000)
line4 = SVGzLine(400,123,695,329)
frame.addNode(nd1)
frame.addNode(nd2)
frame.addNode(nd3)
frame.addNode(nd4)
frame.writeToPNG("frame1.png")
frame.saveToFile("mysgggg.svg")
frame2.addNode(line1)
frame2.addNode(line2)
frame2.addNode(line3)
frame2.addNode(line4)
frame2.writeToPNG("frame2.png")
animation.addKeyFrame(frame,0)
animation.addKeyFrame(frame2,10)
animation.addClip(clip1())
#MyAnimator.writeVideo(animation,"andyandrobert.wav")
