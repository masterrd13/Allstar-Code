#Paint Shop
# Developed by Nathan and Richard
from Processing import *
#Creates Window
window(500,500)
background(255,255,255)

#Uses the draw function to allow user input
# Draw function
def draw():
    if onMousePressed == True:
        circleSize=25
        colorValue=0
        if colorValue==0: #Black
            fill(255,0,0)
        ellipse(mouseX(),mouseY(),circleSize,circleSize)
    
#Draws based on Mouse coords(mouseX,mouseY).
def doMousePressed():
    print( 'mouse pressed at ' + str(mouseX()) + ', ' + str(mouseY()) )
onMousePressed += doMousePressed

