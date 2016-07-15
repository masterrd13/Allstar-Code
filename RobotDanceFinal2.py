from Myro import *
def Dance1():
    i = 0
    while i < 4 :
        forward (2, 1)
        backward (2, 1)
        turnBy (90)
        i = i + 1
        i=0
def Dance2():
    while i < 2 :
        turnRight(2,1)
        forward(2,1)
        turnLeft(2,1)
        forward(2,1)
        i = i + 1
        i=0
def Dance3():      
    i=0
    while i < 6 :
        backward (2, 1)
        turnLeft(2,1)
        turnBy (70)
        turnRight(2,1)
        forward(2,1)
        i = i + 1

def Dance4():
    i=0
    while i < 4 :
        forward (2,1)
        turnBy (80)
        turnLeft (2,1)
        forward (2,1)
        i=i+1
Dance1()
Dance2()
Dance3()
Dance4()
forward (2,1)
backward(2,1)
forward (2,1)
backward(2,1)
  
    