#Paint Shop
# Developed by Nathan and Richard
from Processing import *
#Creates Window
window(500,500)
background(255,255,255)
noStroke()
#Makes black square
fill(0,0,0)
rect(0,0,100,100);
#Makes red square
fill(255,0,0)
rect(100,0,100,100);
#Makes green square
fill(0,255,0)
rect(200,0,100,100);
#Makes blue square
fill(0,0,255)
rect(300,0,100,100);
#Makes yellow square
fill(255,255,0)
rect(400,0,100,100);
#Allows the user to draw when mouse is pressed
while True:
    if isMousePressed()== True and mouseY() >100:
        noStroke()
        circleSize=25
        colorValue=0
        if colorValue==0: #Black
            fill(0,0,0)
        elif colorValue==1: #Red
            fill(255,0,0)
        elif colorValue==2: #Green
            fill(0,255,0)
        elif colorValue==3: #Blue
            fill(0,0,255)
        elif colorValue==3: #Green
            fill(255,255,0)
        ellipse(mouseX(),mouseY(),circleSize,circleSize)
#Draws based on Mouse coords(mouseX,mouseY).
def doMousePressed():
    print( 'mouse pressed at ' + str(mouseX()) + ', ' + str(mouseY()) )
onMousePressed += doMousePressed

