from graphics import *
import graphics
import time

int_sizemod = 1

win = graphics.GraphWin("Title",600*int_sizemod,200*int_sizemod)

top_left_third = Rectangle(Point(0*int_sizemod,0*int_sizemod),Point(200*int_sizemod,200*int_sizemod))
#top_left_third.setOutline("black")
#top_left_third.draw(win)

top_middle_third = Rectangle(Point(200*int_sizemod,0*int_sizemod),Point(400*int_sizemod,200*int_sizemod))
#top_middle_third.setOutline("black")
#top_middle_third.draw(win)

top_right_third = Rectangle(Point(400*int_sizemod,0*int_sizemod),Point(600*int_sizemod,200*int_sizemod))
#top_right_third.setOutline("black")
#top_right_third.draw(win)

#bot_left_third = Rectangle(Point(0*int_sizemod,200*int_sizemod),Point(200*int_sizemod,400*int_sizemod))
#bot_left_third.setOutline("black")
#bot_left_third.draw(win)

#bot_middle_third = Rectangle(Point(200*int_sizemod,200*int_sizemod),Point(400*int_sizemod,400*int_sizemod))
#bot_middle_third.setOutline("black")
#bot_middle_third.draw(win)

#bot_right_third = Rectangle(Point(400*int_sizemod,200*int_sizemod),Point(600*int_sizemod,400*int_sizemod))
#bot_right_third.setOutline("black")
#bot_right_third.draw(win)



x = 0

circle_radius = 15
x_modifier = 0
y_modifier = 0

#startspawn = Point(win.getHeight-15,win.getWidth-15)
#startspawn = Point(300,150)

startspawn = Point(585,185)

    
for x in range(0,2):
    for i in range(0,20):   #columns draw loop ( single line)
        circlespawn = Circle(Point(585-x_modifier,185-y_modifier),15)
        #startspawn = Point(startspawn.getX()+30,startspawn.getY()+30)
        circlespawn.setFill("black")
        circlespawn.draw(win)
    y_modifier = y_modifier - 30
    
     
#for i in range(0,20):
#    #y_modifier = y_modifier + 15
#    circlespawn = Circle(Point(585-x_modifier,185-y_modifier),15)
#    #startspawn = Point(startspawn.getX()+30,startspawn.getY()+30)
#    circlespawn.setFill("black")
#    circlespawn.draw(win)
#    x_modifier = x_modifier + 30


#spawncirclelocation = Circle(Point(startspawn+x_modifier,startspawn+y_modifier),15)
    





while True:
    mousepoint = win.getMouse()

    for x in range(0,3):
        if(mousepoint.getX()>200 and mousepoint.getX()<400):
            color = "green"
        elif(mousepoint.getX()>400 and mousepoint.getX()>200):
            color = "blue"
        else:
            color = "red"
        x = x + 1

    circle = Circle(mousepoint, 30)
    circle.setFill(color)
    circle.draw(win)

