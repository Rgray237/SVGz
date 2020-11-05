import unittest
from SVGz import *
from SVGzFrame import *

class MyFirsttests(unittest.TestCase):


    ##Mark Node Tests
    def test_init_node(self):
        self.assertEqual(SVGzNode().svgTxt,"")



    ##Mark Line Tests
    def test_init_line(self):
        self.assertEqual(SVGzLine(0,0,0,0).svgTxt,f'<line x1="0" y1="0" x2="0" y2="0" stroke="red"></line>\n')
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
        self.assertEqual(mrph.getFrameAtTime(3,10).getTxt(),resultFram.getTxt())


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
        mrph = SVGzMorph(fram1,fram2)
        fram1.addNode(line1)
        fram1.addNode(line2)
        fram2.addNode(line3)
        fram2.addNode(line4)
        duration = 10
        anim.setTimelineDuration(duration)
        anim.timeline.addFeature(mrph,0,10)
        svgz.generateMoviePyClipFromAnimation(anim)
        svgz.saveFrameAtTime(0,anim,"frame1")
        svgz.saveFrameAtTime(8,anim,"frame2")
        self.assertTrue(svgz.writeVideo(anim,"andyandrobert.wav"))



if __name__ == '__main__':
    unittest.main()
