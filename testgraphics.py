import graphics
import time
win = graphics.GraphWin("title",500,500)

#c = graphics.Circle(graphics.Point(500,500), 50)
#c.setFill("red")
#c.draw(win)

#larm = graphics.Line(500, 600)
#larm.draw(win)
#larm.setFill("blue")


def drawlarm(larmsrt1,larmsrt2,larmend1,larmend2):
    larmsrt = graphics.Point(larmsrt1,larmsrt2)
    larmend = graphics.Point(larmend1,larmend2)
    graphics.Line(larmsrt,larmend).draw(win)


def drawrarm(rarmsrt1,rarmsrt2,rarmend1,rarmend2):
    rarmsrt = graphics.Point(rarmsrt1,rarmsrt2)
    rarmend = graphics.Point(rarmend1,rarmend2)
    graphics.Line(rarmsrt,rarmend).draw(win)


def drawrleg(rlegsrt1,rlegsrt2,rlegend1,rlegend2):
    rlegsrt = graphics.Point(rlegsrt1,rlegsrt2)
    rlegend = graphics.Point(rlegend1,rlegend2)
    graphics.Line(rlegsrt,rlegend).draw(win)


def drawlleg(llegsrt1,llegsrt2,llegend1,llegend2):
    llegsrt = graphics.Point(llegsrt1,llegsrt2)
    llegend = graphics.Point(llegend1,llegend2)
    graphics.Line(llegsrt,llegend).draw(win)

def drawbody(bodystr1,bodystr2,bodyend1,bodyend2):
    bodystr = graphics.Point(bodystr1,bodystr2)
    bodyend = graphics.Point(bodyend1,bodyend2)
    graphics.Line(bodystr,bodyend).draw(win)

print("Lets draw this figure out...")





while True:
    time.sleep(500)