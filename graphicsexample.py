from graphics import *
import graphics
import time

int_sizemod = 1

win = graphics.GraphWin("title",500*int_sizemod,500*int_sizemod)

#graphics.Rectangle(100,100).draw(win)

bodyoriginvert = 200*int_sizemod
bodyoriginhort = 100*int_sizemod

########## Body Drawing
int_body_hor_start = 250*int_sizemod #Horizontal Coord of the Top of the body
int_body_hor_end = 250*int_sizemod #Horizontal Coord of the Bottom of the body
int_body_ver_start = 150*int_sizemod #Vertical Coord of the top of the body
int_body_ver_end = 250*int_sizemod #Vertical Coord of the bottom of the body
########## Head Drawing
int_headhorcnt = 250*int_sizemod #Horizontal Coord of the center of the head
int_headvercnt = 125*int_sizemod #Vertical Coord of the center of the head
int_headradius = 25 *int_sizemod #Radius value of the head
########## Right Arm Drawing
int_right_arm_hor_start = 250*int_sizemod
int_right_arm_ver_start = 200*int_sizemod
int_right_arm_hor_end = 175*int_sizemod
int_right_arm_ver_end = 150*int_sizemod
########## Left Arm Drawing
int_left_arm_hor_start = 250*int_sizemod
int_left_arm_ver_start = 200*int_sizemod
int_left_arm_hor_end = 325*int_sizemod
int_left_arm_ver_end = 250*int_sizemod
########## Right Leg Drawing
int_right_leg_hor_start = 250*int_sizemod
int_right_leg_ver_start = 250*int_sizemod
int_right_leg_hor_end = 280*int_sizemod
int_right_leg_ver_end = 300*int_sizemod
########## Left Leg Drawing
int_left_leg_hor_start = 250*int_sizemod
int_left_leg_ver_start = 250*int_sizemod
int_left_leg_hor_end = 220*int_sizemod
int_left_leg_ver_end = 300*int_sizemod

message = Text(Point(100,100), "Hello!").draw(win)
time.sleep(5)
message.undraw()

Rectangle = graphics.Rectangle(Point(150*int_sizemod,150*int_sizemod),Point(350*int_sizemod,350*int_sizemod))
Rectangle.draw(win)
time.sleep(2)
message = Text(Point(230,230), "Test Test!")
time.sleep(2)
message.undraw()

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

time.sleep(500)