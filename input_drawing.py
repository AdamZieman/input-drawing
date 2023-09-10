# input_drawing.py
# An interactive window that will create a square with a user-defined size,
# location, and amount of random colored stripes.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 7

# Author: Adam Zieman
# Date: April 13, 2021

from graphics import *
from random import randrange

def main():
    # creates the window
    win = GraphWin("Input Drawing",1000,750)
    win.setCoords(0,0,100,75)

    # text to instruct user what to do
    stepText = Text(Point(50,10),"Enter size of square's side, then click mouse")
    stepText.setSize(16)
    stepText.draw(win)

    # entry box for user to enter information
    inputText = Entry(Point(50,5),5)
    inputText.setFill("white")
    inputText.setText("0")
    inputText.setSize(14)
    inputText.draw(win)

    # WINDOW PAUSE
    win.getMouse()

    # extracts user input and converts into into a string variable
    sizeString = inputText.getText()
    size = float(sizeString)

    # calculates half of the number entered by the user
    halfSize = size / 2

    # updates user instruction text
    stepText.setText("Click center of square")

    # WINDOW PAUSE
    # mouse click information saved under <center>
    center = win.getMouse()

    # extracts the (x,y) coord from <center>
    xCenter = center.getX()
    yCenter = center.getY()

    # draws a square centered at the mouse click location with a length set to the user's input
    # square's corners window location = (<xCenter> or <yCenter>) +/- <halfSize>
    Rectangle(Point(xCenter-halfSize,yCenter-halfSize),
              Point(xCenter+halfSize,yCenter+halfSize)).draw(win)

    # updates user instruction text
    stepText.setText("Type the number of stripes to draw, then click anywhere")

    # WINDOW PAUSE
    win.getMouse()

    # extracts user input and converts into into a string variable
    stripeString = inputText.getText()
    stripe = int(stripeString)

    # stripeHeight = square height / number of stripes
    stripeHeight = size / stripe

    # initialize variables
    x1Stripe = xCenter - halfSize
    y1Stripe = yCenter - halfSize
    x2Stripe = xCenter + halfSize
    y2Stripe = y1Stripe + stripeHeight
    red = randrange(0,256)
    green = randrange(0,256)
    blue = randrange(0,256)
    myColor = color_rgb(red,green,blue)

    # creates a colored rectangle within the the drawn square relative to the amount of "stripes"
    # to be drawn in the square
    stripeDraw = Rectangle(Point(x1Stripe,y1Stripe),Point(x2Stripe,y2Stripe))
    stripeDraw.setFill(myColor)
    stripeDraw.draw(win)

    # creates the remaing amount of requested stripes
    for i in range(stripe - 1):
        # moves location of next stripe up
        y1Stripe = y2Stripe
        y2Stripe = y1Stripe + stripeHeight
        
        # random color
        red = randrange(0,256)
        green = randrange(0,256)
        blue = randrange(0,256)
        myColor = color_rgb(red,green,blue)

        # draws the colored rectangle
        stripeDraw = Rectangle(Point(x1Stripe,y1Stripe),Point(x2Stripe,y2Stripe))
        stripeDraw.setFill(myColor)
        stripeDraw.draw(win)
        
    # updates user instruction text
    stepText.setText("Click anywhere to close")

    # WINDOW PAUSE
    win.getMouse()

    # closes window
    win.close()
    
main()



