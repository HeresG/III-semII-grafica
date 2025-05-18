# se va trasa :
# a) un dreptunghi
# b) un trapez
# c) un romb
# d) un semicerc
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(2)

### a. Dreptunghi
def deseneaza_dreptunghi(x, y):
    pen.color("blue", "lightblue")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(60)
        pen.left(90)
    pen.end_fill()

### b. Trapez
def deseneaza_trapez(x, y):
    baza_mica = 60
    baza_mare = 120
    inaltime = 50
    diferenta = (baza_mare - baza_mica) / 2

    pen.color("green", "lightgreen")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()

    # Baza mică sus
    pen.setheading(0)
    pen.forward(baza_mica)

    # Latura oblică dreapta
    pen.goto(x + baza_mica + diferenta, y - inaltime)

    # Baza mare jos
    pen.goto(x - diferenta, y - inaltime)

    # Latura oblică stângă
    pen.goto(x, y)

    pen.end_fill()

### c. Romb
def deseneaza_romb(x, y):
    pen.color("red", "salmon")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(80)
        pen.left(60)
        pen.forward(80)
        pen.left(120)
    pen.end_fill()

### d. Semicerc
def deseneaza_semicerc(x, y):
    pen.color("purple", "violet")
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.circle(50, 180)  # rază 50, unghi 180°
    pen.goto(x, y)
    pen.end_fill()


deseneaza_dreptunghi(-200, 100)
deseneaza_trapez(0, 170)
deseneaza_romb(-200, -50)
deseneaza_semicerc(50, -50)

pen.hideturtle()
screen.exitonclick()
