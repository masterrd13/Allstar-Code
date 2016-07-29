##This program takes any image, and converts it to the Hope poster color scheme
from Myro import* 
#These set the color values that we're going to use later.
ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)
#This line saves the image in a variable for later use.
Photo = makePicture("Trump.JPG")
#This line gets the list of RGB info from the saved image
Pixels = getPixels(Photo)
#This then resets all the color values in the selected image to the four selected colors
for i in Pixels:
    if getGray(i)>180:
        setColor(i,ObamaYellow)
    elif getGray(i)>120:
        setColor(i,ObamaBlue)
    elif getGray(i)>60:
        setColor(i,ObamaRed)
    else:
        setColor(i,ObamaDarkBlue)
show(Photo)
