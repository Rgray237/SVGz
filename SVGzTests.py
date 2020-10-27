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



    ##Mark Animation Tests
    def test_init_animation(self):
        self.assertTrue(SVGzAnimation()!=None)
    def test_animation_add_key_frame(self):
        anim = SVGzAnimation()
        self.assertIsNone(anim.addKeyFrame(SVGzFrame(),3))
    def test_animation_set_duration(self):
        anim = SVGzAnimation()
        self.assertEqual(anim.setDuration(20.4),20.4)
    def test_animation_get_fps(self):
        self.assertEqual(SVGzAnimation().getFPS(),60)

    def test_key_frames_morphable(self):
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
        self.assertFalse(SVGzAnimation().areKeyFramesMorphable(fram1,fram2))
        fram2.addNode(line4)
        self.assertTrue(SVGzAnimation().areKeyFramesMorphable(fram1,fram2))



    def test_animation_morph_btwn_key_frames(self):
        anim = SVGzAnimation()
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
        fram2.addNode(line4)
        if anim.areKeyFramesMorphable(fram1,fram2):
            self.assertEqual(anim.morphedFrameAtTime(5,fram1,fram2,duration).getTxt(),f'<svg viewBox="-0 -0 1920 1080" xmlns="http://www.w3.org/2000/svg">\n<line x1="150.0" y1="11.5" x2="52.5" y2="525.0" stroke="red"></line>\n<line x1="205.0" y1="71.5" x2="367.5" y2="214.5" stroke="red"></line>\n</svg>')
        else:
            self.assertTrue(False)


    def test_get_most_recent_key_frame_at_time(self):
        anim= SVGzAnimation()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        duration = 10
        anim.setDuration(10)
        anim.addKeyFrame(fram1,0)
        anim.addKeyFrame(fram2,7)
        anim.addKeyFrame(fram1,10)

        self.assertEqual(anim.getMostRecentKeyFrame(3),fram1)
        self.assertEqual(anim.getMostRecentKeyFrame(7),fram2)
        self.assertEqual(anim.getMostRecentKeyFrame(8),fram2)
        self.assertEqual(anim.getMostRecentKeyFrame(10),fram1)


    def test_get_animation_frame_at_time(self):
        anim= SVGzAnimation()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        duration = 10
        anim.setDuration(10)
        anim.addKeyFrame(fram1,0)
        anim.addKeyFrame(fram2,7)

        self.assertEqual(anim.getFrameAtTime(0),fram1)
        self.assertEqual(anim.getFrameAtTime(3),fram1)
        self.assertEqual(anim.getFrameAtTime(7),fram2)


    #MARK test morphs
    def test_create_morph(self):
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        duration = 10
        anim.setDuration(10)
        anim.addKeyFrame(fram1,0)
        anim.addKeyFrame(fram2,7)
        morph = SVGzMorph(fram1,fram2)


    #MARK test SVGz overall
    def test_write_video(self):
        anim = SVGzAnimation()
        svgz = SVGz()
        fram1 = SVGzFrame()
        fram2 = SVGzFrame()
        line1 = SVGzLine(0,0,10,50)
        line2 = SVGzLine(10,20,40,100)
        fram1.addNode(line1)
        fram2.addNode(line2)
        duration = 10
        anim.setDuration(10)
        anim.addKeyFrame(fram1,0)
        anim.addKeyFrame(fram2,7)
        svgz.generateMoviePyClipFromAnimation(anim)
        svgz.saveFrameAtTime(3,anim,"frame1")
        svgz.saveFrameAtTime(8,anim,"frame2")
        #self.assertTrue(svgz.writeVideo(anim,"andyandrobert.wav"))



if __name__ == '__main__':
    unittest.main()
