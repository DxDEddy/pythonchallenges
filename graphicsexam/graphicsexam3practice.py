from graphics import *
import graphics
import time

int_sizemod = 1
color = "black"

win = graphics.GraphWin("Title",600*int_sizemod,200*int_sizemod)

top_left_third = Rectangle(Point(0*int_sizemod,0*int_sizemod),Point(200*int_sizemod,200*int_sizemod))
top_middle_third = Rectangle(Point(200*int_sizemod,0*int_sizemod),Point(400*int_sizemod,200*int_sizemod))
top_right_third = Rectangle(Point(400*int_sizemod,0*int_sizemod),Point(600*int_sizemod,200*int_sizemod))

circle_radius = 15
x_modifier = 585
y_modifier = 185

def getmousepoint(mousepoint):
    global color

    if(mousepoint.getX()>200 and mousepoint.getX()<400):
        color = "green"
    elif(mousepoint.getX()>400 and mousepoint.getX()>200):
        color = "blue"
    else:
        color = "red"
    return color

startspawn = Point(x_modifier,y_modifier)

for i in range(0,2):
    x_modifier = 585
    for i in range(0,20):
        mousepoint = win.getMouse()
        getmousepoint(mousepoint)
        circle = Circle(Point(x_modifier,y_modifier),circle_radius)
        circle.setFill(color)
        circle.draw(win)
        x_modifier = x_modifier - 30
    y_modifier = y_modifier - 30



























time.sleep(500)

#for i in range(0,20):
#    circle = Circle(Point(x_modifier,y_modifier),circle_radius)
#    circle.setFill("Black")
#    circle.draw(win)
#    x_modifier = x_modifier - 30