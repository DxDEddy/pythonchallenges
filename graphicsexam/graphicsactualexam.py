from graphics import *
import graphics
import time
import os

color = "orange"

win = graphics.GraphWin("Circles",800,600)

red_square = Rectangle(Point(0,0),Point(200,600))
white_square = Rectangle(Point(200,0),Point(400,600))
blue_square = Rectangle(Point(400,0),Point(600,600))
green_square = Rectangle(Point(600,0),Point(800,600))


#
#
##### TASK 1
#
#

def getmousepoint(mousepoint):
    global color

    if(mousepoint.getX()>0 and mousepoint.getX()<200):
        color = "red"
    elif(mousepoint.getX()>200 and mousepoint.getX()<400):
        color = "white"
    elif(mousepoint.getX()>400 and mousepoint.getX()<600):
        color = "blue"
    elif(mousepoint.getX()>600 and mousepoint.getX()<800):
        color = "green"
    else:
        color = "pink"

    return color

def circles():
    for i in range(0,15):
        mousepoint = win.getMouse()
        getmousepoint(mousepoint)
        circle = Circle(Point(mousepoint.getX(),mousepoint.getY()),40)
        circle.setFill(color)
        circle.draw(win)

#circles()

#
#
### TASK 2
#
#

def circles2():
    start_draw = 280
    x_axis_circle = start_draw
    y_axis_circle = 40

    def drawrow(x_axis_circle,y_axis_circle,color):
        for i in range(0,4):
            startspawn = Point(x_axis_circle,y_axis_circle)
            drawcircle = Circle(startspawn,40)
            mousepoint = win.getMouse()

            if(mousepoint.getX()>0 and mousepoint.getX()<200):
                color = "red"
            elif(mousepoint.getX()>200 and mousepoint.getX()<400):
                color = "white"
            elif(mousepoint.getX()>400 and mousepoint.getX()<600):
                color = "blue"
            elif(mousepoint.getX()>600 and mousepoint.getX()<800):
                color = "green"

            drawcircle.setFill(color)
            drawcircle.draw(win)

            x_axis_circle = x_axis_circle + 80

    y_axis_increment = 40
    for i in range(1,5):
        drawrow(x_axis_circle,y_axis_increment,color)
        y_axis_increment = y_axis_increment + 80


circles2()


os.exit()

time.sleep(500)