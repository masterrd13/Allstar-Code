#Developed by Richard
from Processing import*
from random import*
#Creates Window
window(700,700)
background(0,0,0)
ballX=200
ballY=400
speed=30
Xaxis = choice([True,False])
Yaxis= choice([True,False])
while True:
    noStroke()  
    #Decides ball movement 
    fill(255, 255, 255)
    ellipse(ballX, ballY, 50, 50)
    if Xaxis== True:
        ballX+=speed
    elif Xaxis== False:
        ballX-=speed
    if Yaxis == True:
        ballY+=speed
    elif Yaxis == False:
        ballY-=speed
#Controls collisions
    if ballX>670:
        Xaxis= False
    if ballX<35:
        Xaxis= True
    if ballY<35:
        Yaxis= True
    if ballY>670:
        Yaxis= False
    delay(30)
    background(0,0,0)
   
    
    
    
