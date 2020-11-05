import gizeh as gz
import numpy as np
import moviepy.editor as mpy
import cairosvg as csvg
from PIL import Image as pilimg
from PIL import ImageFilter
import io

class SVGzNode:

    def __init__(self):
        self.svgTxt = ""

    def getSVGTxt(self):
        self.updateSVGTxt()
        return self.svgTxt

    def setSVGTxt(self,txt):
        self.svgTxt = txt
        return

    def updateSVGTxt(self):
        return

    def getNodeType(self):
        return

    def getMorphables(self):
        return

    def setMorphables(self):
        return

class SVGzLine(SVGzNode):

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.stroke="red"
        self.svgTxt = f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.stroke}"></line>\n'

    def updateSVGTxt(self):
        self.svgTxt = f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" stroke="{self.stroke}"></line>\n'

    def getNodeType(self):
        return "LINE"

    def getMorphables(self):
        return [self.x1,self.y1,self.x2,self.y2]

    def setMorphables(self,morphList):
        self.x1 = morphList[0]
        self.y1 = morphList[1]
        self.x2 = morphList[2]
        self.y2 = morphList[3]
        return




class SVGzFrame:


    def __init__(self):
        self.image_pad = 0
        self.image_width = 1920
        self.image_height = 1080
        self.header = f'<svg viewBox="-{self.image_pad} -{self.image_pad} {self.image_width + 2 * self.image_pad} {self.image_height + 2 * self.image_pad}" xmlns="http://www.w3.org/2000/svg">\n'
        self.footer = f'</svg>'
        self.nodes = []
        self.svgTxt = self.getTxt()
        self.t = 0

    def addNode(self,nd):
        self.nodes.append(nd)
        return

    def clearFrame(self):
        self.nodes.clear()
        return

    def getTxt(self):
        nodesTxt = ""
        for x in self.nodes:
            nodesTxt += x.getSVGTxt()
        return self.header + nodesTxt + self.footer


    def saveToFile(self,filename:str):
        file = open(filename,'w')
        file.write(self.getTxt())
        return

    def writeToPNG(self, filename:str):
        csvg.svg2png(self.getTxt(), write_to=filename)
        return

    def writeAntiAliasedToPNG(self,filename:str):
        img = self.getPILImage()
        img.save(filename)
        return

    def applyFilterToPILImg(self,img):
        img1 = img.filter(ImageFilter.GaussianBlur)
        return img1


    def getPILImage(self):
        temp = csvg.svg2png(self.getTxt())
        image = pilimg.open(io.BytesIO(temp))
        return image


    def PILToNumpy(self,img):
        return np.array(img)

    def getNumpyArrayFromSVG(self, filename:str):
        img = self.getPILImage(filename)
        return self.PILToNumpy(img)

    def getNumpyArray(self):
        img = self.getPILImage()
        return self.PILToNumpy(img)

    def getNumpyArrayFromPNG(self, filename:str):
        img = pilimg.open(filename)
        return self.PILToNumpy(img)


#print(frame.getTxt())
#frame.saveToFile("mySVG.svg")
#frame.writeToPNG("")
#frame.getNumpyArray().show()
#frame.getNumpyArrayFromSVG("mySVG.svg").show()
#numpyArr = frame.getNumpyArrayFromPNG("out.png")
#numpyArr.show()
