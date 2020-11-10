import unittest
from SVGz import *
from SVGzFrame import *

class MyFirsttests(unittest.TestCase):


    ##Mark Node Tests
    def test_init_node(self):
        self.assertEqual(SVGzNode().svgTxt,"")



    ##Mark Line Tests
    def test_init_line(self):
        self.assertEqual(SVGzLine(0,0,0,0).getSVGTxt(),f'<line x1="0" y1="0" x2="0" y2="0" stroke="red"></line>\n')
    def test_line_svg_update(self):
        line = SVGzLine(0,0,0,0)
        line.x1 = 4
        line.stroke = "green"
        self.assertEqual(line.getSVGTxt(),f'<line x1="4" y1="0" x2="0" y2="0" stroke="green"></line>\n')
    def test_line_get_node_type(self):
        line = SVGzLine(0,0,0,0)
        self.assertEqual(line.getNodeType(),"LINE")

    def test_line_get_morphables(self):
        line = SVGzLine(0,0,0,0)
        self.assertEqual(line.getMorphables(),[0,0,0,0])

    ##Mark Ellipse Tests
    def test_init_ellipse(self):
        self.assertEqual(SVGzEllipse(0,0,0,0).getSVGTxt(),f'<ellipse cx="0" cy="0" rx="0" ry="0" stroke="green" fill="none"></ellipse>\n')

    def test_ellipse_svg_update(self):
        line = SVGzEllipse(0,0,0,0)
        line.cx = 4
        line.stroke = "green"
        self.assertEqual(line.getSVGTxt(),f'<ellipse cx="4" cy="0" rx="0" ry="0" stroke="green" fill="none"></ellipse>\n')

    def test_ellipse_get_node_type(self):
        line = SVGzEllipse(0,0,0,0)
        self.assertEqual(line.getNodeType(),"ELLIPSE")

    def test_ellipse_get_morphables(self):
        ELLIPSE = SVGzEllipse(0,0,10,0)
        self.assertEqual(ELLIPSE.getMorphables(),[0,0,10,0])


    ##MARK Polyline Tests
    def test_init_polyline(self):
        polyline = SVGzPolyline([(0,100)])
        self.assertEqual(polyline.getSVGTxt(),f'<polyline points="0,100" stroke="green" fill="none"></polyline>\n')

    def test_polyline_svg_update(self):
        polyline = SVGzPolyline([(0,100)])
        polyline.setArray([(0,100),(50,70),(60,47),(25,0)])
        self.assertEqual(polyline.getSVGTxt(),f'<polyline points="0,100 50,70 60,47 25,0" stroke="green" fill="none"></polyline>\n')

    def test_polyline_get_morphables(self):
        polyline = SVGzPolyline([(0,100),(50,70),(60,47)])
        self.assertEqual(polyline.getMorphables(),[0,100,50,70,60,47])

    def test_polyline_set_morphables(self):
        polyline = SVGzPolyline([(0,100),(50,70),(60,47)])
        polyline.setMorphables([10,20,30,40,50,60])
        self.assertEqual(polyline.getMorphables(),[10,20,30,40,50,60])


    ##Mark Frame Tests
    def test_init_frame(self):
        self.assertEqual(SVGzFrame().svgTxt,f'<svg viewBox="-0 -0 1920 1080" xmlns="http://www.w3.org/2000/svg">\n</svg>')

    def test_clear_frame(self):
        fram = SVGzFrame()
        line1 = SVGzLine(0,1,2,3)
        fram.addNode(line1)
        self.assertEqual(len(fram.nodes),1)
        fram.clearFrame()
        self.assertEqual(len(fram.nodes),0)


    def test_set_nodes(self):
        fram = SVGzFrame()
        line1 = SVGzLine(0,1,2,3)
        line2 = SVGzLine(0,0,0,0)
        self.assertEqual(fram.getNodes(),[])
        nds = []
        nds.append(line1)
        nds.append(line2)
        fram.setNodes(nds)
        self.assertEqual(fram.getNodes(),[line1,line2])
        nds.clear()
        nds.append(line2)
        fram.setNodes(nds)
        self.assertEqual(fram.getNodes(),[line2])

    ##Mark Animation Tests
    def test_init_animation(self):
        self.assertTrue(SVGzAnimation()!=None)
    def test_animation_set_duration(self):
        anim = SVGzAnimation()
        self.assertEqual(anim.setTimelineDuration(20.4),20.4)
    def test_animation_get_fps(self):
        self.assertEqual(SVGzAnimation().getFPS(),60)

    def test_frames_morphable(self):
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        line3 = SVGzLine(300,23,95,1000)
        line4 = SVGzLine(400,123,695,329)
        duration = 10
        fram1.addNode(line1)
        fram1.addNode(line2)
        fram2.addNode(line3)
        self.assertFalse(SVGzAnimation().areFramesMorphable(fram1,fram2))
        fram2.addNode(line4)
        self.assertTrue(SVGzAnimation().areFramesMorphable(fram1,fram2))
        polyline1 = SVGzPolyline([(0,10)])
        polyline2 = SVGzPolyline([(0,10),(23,45)])
        fram1.addNode(polyline1)
        fram2.addNode(polyline2)
        self.assertFalse(SVGzAnimation().areFramesMorphable(fram1,fram2))
        polyline1.setArray([(0,23),(10,42)])
        self.assertTrue(SVGzAnimation().areFramesMorphable(fram1,fram2))



    def test_get_animation_frame_at_time(self):
        anim= SVGzAnimation()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        duration = 10
        anim.setTimelineDuration(10)



    #MARK test timeline
    def test_add_feature(self):
        timeline = SVGzTimeline(100)
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        fram1.addNode(line1)
        fram2.addNode(line2)
        duration = 10
        timeline.addFeature(SVGzMorph(fram1,fram2),0,duration)


    #MARK test morphs
    def test_morph(self):
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        line3 = SVGzLine(300,23,95,1000)
        line4 = SVGzLine(400,123,695,329)
        resultFram = SVGzFrame()
        line5 = SVGzLine(90.0,6.9,35.5,335.0)
        line6 = SVGzLine(127.0,50.9,236.5,168.7)
        resultFram.addNode(line5)
        resultFram.addNode(line6)
        fram1.addNode(line1)
        fram1.addNode(line2)
        fram2.addNode(line3)
        fram2.addNode(line4)
        mrph = SVGzMorph(fram1,fram2)
        self.assertEqual(mrph.type,"Morph")
        self.assertEqual(mrph.getFirst(),fram1)
        self.assertEqual(mrph.getSecond(),fram2)
        self.assertEqual(mrph.getFrameAtTime(3,10).getSVGTxt(),resultFram.getSVGTxt())

    def test_circle_and_line(self):
        anim = SVGzAnimation()
        svgz = SVGz()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,100,300)
        circle1 = SVGzEllipse(100,100,10,10)
        line2 = SVGzLine(100,100,30,12)
        circle2 = SVGzEllipse(0,0,30,30)
        fram1.addNode(line1)
        fram1.addNode(circle1)
        fram2.addNode(line2)
        fram2.addNode(circle2)
        mrph = SVGzMorph(fram1,fram2)
        duration = 10
        anim.setTimelineDuration(duration)
        anim.timeline.addFeature(mrph,0,10)
        svgz.generateMoviePyClipFromAnimation(anim)
        svgz.saveFrameAtTime(0,anim,"linenellps1")
        svgz.saveFrameAtTime(8,anim,"linenellps2")
        #self.assertTrue(svgz.writeVideo(anim,"andyandrobert.wav"))


    def test_circle_and_line_and_polyline(self):
        anim = SVGzAnimation()
        svgz = SVGz()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,100,300)
        circle1 = SVGzEllipse(100,100,10,10)
        line2 = SVGzLine(100,100,30,12)
        circle2 = SVGzEllipse(0,0,30,30)
        polyline1 = SVGzPolyline([(500,10),(500,42),(301,450),(790,75),(700,640)])
        polyline2 = SVGzPolyline([(500,10),(534,42),(490,200),(800,100),(900,380)])
        fram1.addNode(line1)
        fram1.addNode(circle1)
        fram1.addNode(polyline1)
        fram2.addNode(line2)
        fram2.addNode(circle2)
        fram2.addNode(polyline2)
        mrph = SVGzMorph(fram1,fram2)
        duration = 10
        anim.setTimelineDuration(duration)
        anim.timeline.addFeature(mrph,0,10)
        svgz.generateMoviePyClipFromAnimation(anim)
        svgz.saveFrameAtTime(0,anim,"linenellpspoly1")
        svgz.saveFrameAtTime(8,anim,"linenellpspoly2")
        #self.assertTrue(svgz.writeVideo(anim,"andyandrobert.wav"))

    #MARK test SVGz overall
    def test_write_video(self):
        anim = SVGzAnimation()
        svgz = SVGz()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        line3 = SVGzLine(300,23,95,1000)
        line4 = SVGzLine(400,123,695,329)
        fram1.addNode(line1)
        fram1.addNode(line2)
        fram2.addNode(line3)
        fram2.addNode(line4)
        mrph = SVGzMorph(fram1,fram2)
        duration = 10
        anim.setTimelineDuration(duration)
        anim.timeline.addFeature(mrph,0,10)
        svgz.generateMoviePyClipFromAnimation(anim)
        svgz.saveFrameAtTime(0,anim,"frame1")
        svgz.saveFrameAtTime(8,anim,"frame2")
        #self.assertTrue(svgz.writeVideo(anim,"andyandrobert.wav"))



if __name__ == '__main__':
    unittest.main()
