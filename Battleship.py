from Processing import* 
from random import*
window(700,700)
board=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#Picks boat location 
Ind1=randrange(0,7)#Picks a list
Ind2=randrange(0,7)#Picks an element in list
board[Ind1][Ind2]=1
#Draws entire grid
rect(0,0,100,100)
squareDraw=0
squareX=0   #Defines x of Square
squareY=0   #Defines y of Square
rowC=0  
fill(65,105,225)
stroke(200,0,0)
while squareDraw<49:
    squareS=100 #Defines square size
    rect(squareX,squareY,squareS,squareS)#Draws square
    squareX+=100
    squareDraw+=1
    rowC+=1
    if rowC==7:
        squareY+=100
        squareX=0
        rowC=0  
Guess=input("Enter your first coordinate")
Guess=float(Guess)
Guess2=input("Enter your second coordinate")
Guess2=float(Guess2)
if Guess==Ind1 and Guess2==Ind2:
    fill(0,255,0)
    Guess=(Guess*100)
    Guess2=(Guess2*100)
    rect(Guess,Guess2,100,100)
    print ("You win!")
elif Guess !=Ind1 or Guess2 != Ind2:
    fill(255,0,0)
    Guess=(Guess*100)
    Guess2=(Guess2*100)
    rect(Guess+10,Guess2+10,80,80)
    print ("You lose")
    
