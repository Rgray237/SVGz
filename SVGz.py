import numpy as np
import copy
from SVGzFrame import *
import moviepy.editor as mpy


class SVGzFeature:
    def __init__(self):
        self.type=""

class SVGzMorph(SVGzFeature):
    def __init__(self,frame1:SVGzFrame,frame2:SVGzFrame):
        self.type="Morph"
        self.frame1 = frame1
        self.frame2 = frame2
        self.newFrame = SVGzFrame()
        self.createNewFrameNodes()

    def createNewFrameNodes(self):
        newNodes = []
        for nd in self.frame1.nodes:
            if nd.getNodeType() == "LINE":
                newNodes.append(SVGzLine(0,0,0,0))
            elif nd.getNodeType() == "ELLIPSE":
                newNodes.append(SVGzEllipse(0,0,0,0))
            elif nd.getNodeType() == "POLYLINE":
                newNodes.append(SVGzPolyline([(0,0),(1,1)]))
        self.newFrame.setNodes(newNodes)
        return

    def getFirst(self):
        return self.frame1

    def getSecond(self):
        return self.frame2

    def getFrameAtTime(self,t,duration):
        newFram = self.newFrame
        #print("Time t: " + str(t)+ " frame1 nodes length:" + str(len(self.frame1.nodes))+ " newFrameNodes length: " + str(len(self.newFrame.nodes)))
        for nd in range(len(self.frame1.nodes)):
            mrphs1 = self.frame1.nodes[nd].getMorphables()
            mrphs2 = self.frame2.nodes[nd].getMorphables()
            numIndices = len(mrphs1)
            newMorphs = []
            for x in range(numIndices):
                value = (mrphs2[x]-mrphs1[x])*t/duration + mrphs1[x]
                newMorphs.append(value)
            newFram.nodes[nd].setMorphables(newMorphs)

        return newFram

class SVGzTimeline:
    def __init__(self,duration):
        self.duration = duration
        self.features = []

    def setDuration(self,time):
        self.duration = time
        return self.duration

    def getDuration(self):
        return self.duration

    def addFeature(self,feature:SVGzFeature,time,duration):
        self.features.append(feature)


class SVGzAnimation:
    def __init__(self):
        self.fps=60
        self.timeline=SVGzTimeline(100)

    def setTimelineDuration(self,time):
        self.timeline.setDuration(time)
        return self.timeline.getDuration()

    def getTimelineDuration(self):
        return self.timeline.getDuration()


    def getFrameAtTime(self,t):
        return        self.timeline.features[0].getFrameAtTime(t,10)


    def areFramesMorphable(self,frame1,frame2):
        nodes1 = frame1.nodes
        nodes2 = frame2.nodes
        if len(nodes1) != len(nodes2):
            return False
        for i in range(len(nodes1)):
            if nodes1[i].getNodeType() != nodes2[i].getNodeType():
                return False
            if nodes1[i].getNodeType() == "POLYLINE":
                if nodes1[i].getNumLines() != nodes2[i].getNumLines():
                    return False

        return True

    def getFPS(self):
        return self.fps


class SVGz:
    def generateMoviePyClipFromAnimation(self,animation:SVGzAnimation):
        def make_frame(t):
            frame = animation.getFrameAtTime(t)
            img = frame.getPILImage()
            img1 = frame.applyFilterToPILImg(img)
            arr = frame.PILToNumpy(img1)
            #arr = antialias(arr)
            return arr[:,:,:3]

        self.mpyClip = mpy.VideoClip(make_frame, duration=animation.getTimelineDuration())
        return

    def saveFrameAtTime(self,time,animation:SVGzAnimation,frameName:str):
        self.mpyClip.save_frame(frameName+".jpeg",t=time)
        return

    def writeVideo(self,animation:SVGzAnimation,AudioFileName:str):
        audioClip = mpy.AudioFileClip(AudioFileName)
        newAudio = audioClip.subclip(0,-120)
        finalVid = self.mpyClip.set_audio(newAudio)
        finalVid.write_videofile("SVGeezeFinalVideo.mp4",fps=60)
        return True
