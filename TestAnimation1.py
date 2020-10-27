import gizeh as gz
import numpy as np
import moviepy.editor as mpy
from SVGeeze import SVGeeze, SVGAnimation


def clip1():
    W,H = 256,256
    DURATION = 2.416666
    NDISKS_PER_CYCLE = 8
    SPEED = .05

    def make_frame(t):
        dt = 1.0*DURATION/2/NDISKS_PER_CYCLE # delay between disks
        N = int(NDISKS_PER_CYCLE/SPEED) # total number of disks
        t0 = 1.0/SPEED # indicates at which avancement to start

        surface = gz.Surface(W,H)
        for i in range(1,N):
            a = (np.pi/NDISKS_PER_CYCLE)*(N-i-1)
            r = np.maximum(0, .05*(t+t0-dt*(N-i-1)))
            center = W*(0.5+ gz.polar2cart(r,a))
            color = 3*((1.0*i/NDISKS_PER_CYCLE) % 1.0,)
            circle = gz.circle(r=0.3*W, xy = center,fill = color,
                                  stroke_width=0.01*W)
            circle.draw(surface)
        contour1 = gz.circle(r=.65*W,xy=[W/2,W/2], stroke_width=.5*W)
        contour2 = gz.circle(r=.42*W,xy=[W/2,W/2], stroke_width=.02*W,
                                stroke=(1,1,1))
        contour1.draw(surface)
        contour2.draw(surface)
        return surface.get_npimage()

    clip = mpy.VideoClip(make_frame, duration=DURATION)
    return clip

def clip2():
    W = H = 128
    D = 2.41666 # duration
    nballs=60

    # generate random values of radius, color, center
    radii = np.random.randint(.1*W,.2*W, nballs)
    colors = np.random.rand(nballs,3)
    centers = np.random.randint(0,W, (nballs,2))

    def make_frame(t):
        surface = gz.Surface(W,H)
        for r,color, center in zip(radii, colors, centers):
            angle = 2*np.pi*(t/D*np.sign(color[0]-.5)+color[1])
            xy = center+gz.polar2cart(W/5,angle) # center of the ball
            gradient = gz.ColorGradient(type="radial",
                         stops_colors = [(0,color),(1,color/10)],
                         xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
            ball = gz.circle(r=1, fill=gradient).scale(r).translate(xy)
            ball.draw(surface)
        return surface.get_npimage()

    clip = mpy.VideoClip(make_frame, duration=D)
    clip.set_position((45,150))
    return clip


MyAnimator = SVGeeze()
animation = SVGAnimation()
animation.addClip(clip1())
animation.addClip(clip2())
MyAnimator
MyAnimator.writeVideo(animation,"andyandrobert.wav")
