from Myro import *
x = input ("Enter a number for size.")
a = input ("How many squares do you want?")
print (x)
print (a)
i = 0
while i < 4 and a > 1:
    penDown("red")
    forward(float(x),1)
    turnBy(90)
    penUp()
    i = i + 1
    a = a - 1
    forward(1,1)
    
    


    

