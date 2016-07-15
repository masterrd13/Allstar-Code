from Myro import *
x = input ("Enter a number for size.")
print (x)
i = 0
while i < 4:
    penDown("red")
    forward(float(x),1)
    turnBy(90)
    penUp()
    i = i + 1
    
   


    

