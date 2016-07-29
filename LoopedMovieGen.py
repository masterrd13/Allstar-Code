from random import *
#Title elements list
ArtList=["The", "A", "The First", "The Second", "The Third","Disney's","Final","The Last","The Amazing","The Cool"  ]
AdjList=["Return", "Revenge","Act" , "Killing", "Destroyer","Death","Rebirth","Awakening","Tales","Beginning"]
CharList=["the Jedi","the Sith","the Suspects","Batman","Spiderman","Elmo","Barney","the Flash","Will Smith","Thomas the Tank Engine"]
#Random Title element selector
i=0
def MovieGen():
    i=0 
    while i<10:
        print (ArtList[randrange(9)], AdjList[randrange(9)],"of",CharList[randrange(9)])
        i=i+1
MovieGen()
