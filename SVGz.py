import gizeh as gz
import numpy as np
import copy
from SVGzFrame import *
import moviepy.editor as mpy


class SVGzMorph:
    def __init__(self,frame1:SVGzFrame,frame2:SVGzFrame):
        self.frame1 = frame1
        self.frame2 = frame2


class SVGzAnimation:
    def __init__(self):
        self.duration=0
        self.fps=60
        self.clips=[]
        self.frames=[]
        self.keyFrames=[]

    def addClip(self, clip:mpy.VideoClip):
        self.clips.append(clip)
        return

    def setDuration(self,time):
        self.duration=time
        return self.duration

    def getDuration(self):
        return self.duration

    def addKeyFrame(self,frame,time):
        self.keyFrames.append([frame,time])
        return

    def getAllClips(self):
        return self.clips

    def getMostRecentKeyFrame(self,t):
        mostRecentT = 0
        mostRecentF = self.keyFrames[0]
        for fram in self.keyFrames:
            if fram[1] <= t and fram[1] > mostRecentT:
                mostRecentT = fram[1]
                mostRecentF = fram
        return mostRecentF[0]

    def getFrameAtTime(self,t):
        if t<self.duration:
            frame = self.getMostRecentKeyFrame(t)
        return frame

    def areKeyFramesMorphable(self,frame1,frame2):
        nodes1 = frame1.nodes
        nodes2 = frame2.nodes
        if len(nodes1) != len(nodes2):
            return False
        for i in range(len(nodes1)):
            if nodes1[i].getNodeType() != nodes2[i].getNodeType():
                return False
        return True

    def morphedFrameAtTime(self,t,frame1,frame2,duration):
        newFrame = SVGzFrame()
        nodes1 = frame1.nodes
        nodes2 = frame2.nodes
        newNodes = []
        for nodInc in range(len(nodes1)):
            newnode = copy.copy(nodes1[nodInc])
            newnode.getMorphables()
            newnode.setMorphables(np.array(nodes1[nodInc].getMorphables())*(1-t/duration) + (t/duration)*np.array(nodes2[nodInc].getMorphables()))
            newFrame.addNode(newnode)
        return newFrame

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

        self.mpyClip = mpy.VideoClip(make_frame, duration=animation.getDuration())
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
