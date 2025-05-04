# se da patratul ABCD, A(0,0), B(0,6), C(6,6), D(6,0)
#a. aflati translatia acestui patrat cu vectorul v(1,2)
#b. rototranslatia patratului ABCD cu unghi 0=45 grade si v(1,2) in jurul lui O.


import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(2)

SCALARE = 40

OFFSET_X = -100
OFFSET_Y = -200

# Coordonatele pătratului ABCD
A = (0, 0)
B = (0, 6)
C = (6, 6)
D = (6, 0)

# Funcții
def translatie(punct, vx, vy):
    return (punct[0] + vx, punct[1] + vy)

def rotatie(punct, unghi):
    radian = math.radians(unghi)
    x, y = punct
    x_prime = x * math.cos(radian) - y * math.sin(radian)
    y_prime = x * math.sin(radian) + y * math.cos(radian)
    return (x_prime, y_prime)

def mutare_pe_ecran(punct):
    return (punct[0] * SCALARE + OFFSET_X, punct[1] * SCALARE + OFFSET_Y)

def deseneaza_patrat(p1, p2, p3, p4, contur, umplere):
    pen.penup()
    pen.goto(mutare_pe_ecran(p1))
    pen.color(contur, umplere)
    pen.begin_fill()
    pen.pendown()
    for punct in [p2, p3, p4, p1]:
        pen.goto(mutare_pe_ecran(punct))
    pen.end_fill()

# Vector translatie și unghi
v = (1, 2)
unghi = 45

# Translatie
A_t = translatie(A, *v)
B_t = translatie(B, *v)
C_t = translatie(C, *v)
D_t = translatie(D, *v)

# Rototranslatie
A_r = translatie(rotatie(A, unghi), *v)
B_r = translatie(rotatie(B, unghi), *v)
C_r = translatie(rotatie(C, unghi), *v)
D_r = translatie(rotatie(D, unghi), *v)

# Desenează pătratele
deseneaza_patrat(A, B, C, D, "blue", "lightblue")           # original
deseneaza_patrat(A_t, B_t, C_t, D_t, "red", "yellow")       # translatat
deseneaza_patrat(A_r, B_r, C_r, D_r, "green", "orange")     # rototranslatat

pen.hideturtle()
screen.exitonclick()
