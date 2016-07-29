#Jackson Pollock Program
#Developed by Richard, Navid, Josh and Danny.

from random import * 

#Creates canvas with 400x400 resolution 
def setup():
    size(400,400)
#Uses the draw function to randomize both the size and color of the brush
#Draws based on Mouse coords(mouseX,mouseY).
def draw():
    global circleSize
    global circleColor
    noStroke()
    circleSize=randrange(5,25)
    colorValue=randrange(0,4)
    if colorValue==0: #Black
        fill(0,0,0)
    elif colorValue==1: #Blue
        fill(119,136,153)
    elif colorValue==2: #Brown
        fill(131,101,8)
    elif colorValue==3: #Yellow
        fill(205,149,12)
    ellipse(mouseX,mouseY,circleSize,circleSize)