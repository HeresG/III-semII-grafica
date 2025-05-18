#se da rotatia x'= x cos O - y sin O , y'= x sin O + y cos O.
# rotiti in jurul axei Ox triunghiul ABC care are coordonatele A(1,3), B(5,6) si C (7,9)

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(1)

A = (1, 3)
B = (5, 6)
C = (7, 9)

theta = 45

theta_rad = math.radians(theta)

def rotatie(punct, theta_rad):
    x, y = punct
    x_prime = x * math.cos(theta_rad) - y * math.sin(theta_rad)
    y_prime = x * math.sin(theta_rad) + y * math.cos(theta_rad)
    return (x_prime, y_prime)

A_rot = rotatie(A, theta_rad)
B_rot = rotatie(B, theta_rad)
C_rot = rotatie(C, theta_rad)

scale = 50

offset_y = -300

def deseneaza_triunghi(p1, p2, p3, contur, umplere):
    pen.penup()
    pen.goto(p1[0] * scale, p1[1] * scale + offset_y)
    pen.color(contur, umplere)
    pen.begin_fill()
    pen.pendown()
    pen.goto(p2[0] * scale, p2[1] * scale + offset_y)
    pen.goto(p3[0] * scale, p3[1] * scale + offset_y)
    pen.goto(p1[0] * scale, p1[1] * scale + offset_y)
    pen.end_fill()

deseneaza_triunghi(A, B, C, "blue", "lightblue")

deseneaza_triunghi(A_rot, B_rot, C_rot, "red", "pink")

pen.penup()
pen.goto(-300, offset_y)
pen.pendown()
pen.goto(300, offset_y)
pen.color("black")
pen.pensize(1)

# Etichete pentru puncte - coordonatele originale
def scrie_eticheta(punct, nume):
    pen.penup()
    pen.goto(punct[0] * scale + 5, punct[1] * scale + offset_y + 5)
    pen.pendown()
    pen.write(f'{nume}({punct[0]},{punct[1]})', font=("Arial", 10, "normal"))

scrie_eticheta(A, "A")
scrie_eticheta(B, "B")
scrie_eticheta(C, "C")

scrie_eticheta(A_rot, "A'")
scrie_eticheta(B_rot, "B'")
scrie_eticheta(C_rot, "C'")

pen.hideturtle()
screen.exitonclick()
