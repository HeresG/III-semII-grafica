from graphics import *

def main():
        win = GraphWin()

        a = Point(25,25)
        b = Point(100,175)
        c = Point(100,100)

        rect = Rectangle(a, b)
        circ = Circle(c, 50)

        rect.setFill("red")
        circ.setFill("blue")
        rect.setOutline("green")
        circ.setOutline("yellow")
        rect.setWidth(5)
        circ.setWidth(10)

        rect.draw(win)
        circ.draw(win)

        raw_input("Press <Enter> to quit")
        win.close()
        
main()
