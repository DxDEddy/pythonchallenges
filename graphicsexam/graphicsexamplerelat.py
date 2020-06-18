from graphics import *
import graphics
import time

int_sizemod = 1.5

win = graphics.GraphWin("title",500*int_sizemod,500*int_sizemod)

#graphics.Rectangle(100,100).draw(win)

#Manually Configured
#int_bodyoriginvert = 250*int_sizemod
#int_bodyoriginhort = 250*int_sizemod
#int_bodyorigin = Point(int_bodyoriginhort,int_bodyoriginvert)

#Click Configured For person
print("Click where you want to draw the person?")
int_bodyorigin = win.getMouse()
int_bodyoriginvert = int_bodyorigin.getY()
int_bodyoriginhort = int_bodyorigin.getX()

#Click configured for whiteboard
print("Click twice to define the size of the whiteboard")
int_whiteboardstart = win.getMouse()
int_whiteboardend   = win.getMouse()


########## Body Drawing
int_body_hor_start = int_bodyoriginhort +0   * int_sizemod #Horizontal Coord of the Top of the body
int_body_hor_end = int_bodyoriginhort   +0   * int_sizemod #Horizontal Coord of the Bottom of the body
int_body_ver_start = int_bodyoriginvert -100 * int_sizemod #Vertical Coord of the top of the body
int_body_ver_end = int_bodyoriginvert   +0   * int_sizemod #Vertical Coord of the bottom of the body
########## Head Drawing
int_headhorcnt = int_bodyoriginhort +0   * int_sizemod #Horizontal Coord of the center of the head
int_headvercnt = int_bodyoriginvert -125 * int_sizemod #Vertical Coord of the center of the head
int_headradius = 25 * int_sizemod #Radius value of the head
########## Right Arm Drawing
int_right_arm_hor_start = int_bodyoriginhort +0   * int_sizemod
int_right_arm_ver_start = int_bodyoriginvert -50  * int_sizemod
int_right_arm_hor_end = int_bodyoriginhort   -75  * int_sizemod
int_right_arm_ver_end = int_bodyoriginvert   -100 * int_sizemod
########## Left Arm Drawing
int_left_arm_hor_start = int_bodyoriginhort +0   * int_sizemod
int_left_arm_ver_start = int_bodyoriginvert -50  * int_sizemod
int_left_arm_hor_end = int_bodyoriginhort   +75  * int_sizemod
int_left_arm_ver_end = int_bodyoriginvert   +0   * int_sizemod
########## Right Leg Drawing
int_right_leg_hor_start = int_bodyoriginhort +0   * int_sizemod
int_right_leg_ver_start = int_bodyoriginvert +0   * int_sizemod
int_right_leg_hor_end = int_bodyoriginhort   +30  * int_sizemod
int_right_leg_ver_end = int_bodyoriginvert   +50  * int_sizemod
########## Left Leg Drawing
int_left_leg_hor_start = int_bodyoriginhort +0   * int_sizemod
int_left_leg_ver_start = int_bodyoriginvert +0   * int_sizemod
int_left_leg_hor_end = int_bodyoriginhort   -30  * int_sizemod
int_left_leg_ver_end = int_bodyoriginvert   +50  * int_sizemod 



########## Body Drawing
int_body_start_pos = graphics.Point(int_body_hor_start,int_body_ver_start)
int_body_end_pos = graphics.Point(int_body_hor_end,int_body_ver_end)
graphics.Line(int_body_start_pos,int_body_end_pos).draw(win).setFill("Grey")
########## Head Drawing
int_head_cnt_pos = graphics.Point(int_headhorcnt,int_headvercnt)
graphics.Circle(int_head_cnt_pos,int_headradius).draw(win)
########## Right Arm Drawing
int_right_arm_start_pos = graphics.Point(int_right_arm_hor_start,int_right_arm_ver_start)
int_right_arm_end_pos = graphics.Point(int_right_arm_hor_end,int_right_arm_ver_end)
graphics.Line(int_right_arm_start_pos,int_right_arm_end_pos).draw(win)
########## Left Arm Drawing
int_left_arm_start_pos = graphics.Point(int_left_arm_hor_start,int_left_arm_ver_start)
int_left_arm_end_pos = graphics.Point(int_left_arm_hor_end,int_right_arm_ver_end)
graphics.Line(int_left_arm_start_pos,int_left_arm_end_pos).draw(win)
########## Right Leg Drawing
int_right_leg_start_pos = graphics.Point(int_right_leg_hor_start,int_right_leg_ver_start)
int_right_leg_end_pos = graphics.Point(int_right_leg_hor_end,int_right_leg_ver_end)
graphics.Line(int_right_leg_start_pos,int_right_leg_end_pos).draw(win)
########## Left Leg Drawing
int_left_leg_start_pos = graphics.Point(int_left_leg_hor_start,int_left_leg_ver_start)
int_left_leg_end_pos = graphics.Point(int_left_leg_hor_end,int_left_leg_ver_end)
graphics.Line(int_left_leg_start_pos,int_left_leg_end_pos).draw(win)

######### Whiteboard Drawing
obj_whiteboard = graphics.Rectangle(int_whiteboardstart,int_whiteboardend)
obj_whiteboard.setFill("White")
obj_whiteboard.draw(win)

######### Pencil Drawing
int_pencilorigin = Point(int_right_arm_hor_end,int_right_arm_ver_end)
int_pencilbodystart = Point(int_right_arm_hor_end+10,int_right_arm_ver_end+15)
int_pencilbodyend   = Point(int_right_arm_hor_end-10,int_right_arm_ver_end-15)
obj_pencilbody = Rectangle(int_pencilbodystart,int_pencilbodyend)
obj_pencilbody.setFill("red")


# message = Text(Point(100,100), "Hello!").draw(win)
# time.sleep(2)
# message = Text(Point(100,100), "Goodbye!").draw(win)
# message.setSize(18)
# message.setFace("arial")
# message.setTextColor("pink")
# time.sleep(2)
# message.setText("Test")
# time.sleep(3)

# message.undraw()

##Whiteboard Draw
# Rectangle = graphics.Rectangle(Point(150*int_sizemod,150*int_sizemod),Point(350*int_sizemod,350*int_sizemod))
# Rectangle.draw(win)
# time.sleep(2)
# message = Text(Point(230,230), "Test Test!")
# time.sleep(2)
# message.undraw()

time.sleep(500)
while True:
    time.sleep(1)
