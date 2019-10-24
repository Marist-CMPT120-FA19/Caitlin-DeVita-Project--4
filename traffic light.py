#Caitlin De Vita
#caitlin.devita1@marist.edu
#Traffic Light (resubmission)


from graphics import *

def main():
    win=GraphWin("Traffic Light")
    outerLamp=Rectangle(Point(50, 50), Point(100, 180))
    outerLamp.setOutline("black")
    outerLamp.setFill("white")
    outerLamp.draw(win)
    
    redLight=Circle(Point(75, 80), 15)
    redLight.setOutline("black")
    redLight.setFill("red")
    redLight.draw(win)
    
    yellowLight=Circle(Point(75, 115), 15)
    yellowLight.setOutline("black")
    yellowLight.setFill("yellow")
    yellowLight.draw(win)
    
    greenLight=Circle(Point(75, 150), 15)
    greenLight.setOutline("black")
    greenLight.setFill("green")
    greenLight.draw(win)



main()
