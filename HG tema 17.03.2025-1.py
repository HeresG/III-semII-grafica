#aflati noile coordonate ale triunghiului ABC, unde A(0,0), B(1,1), C(5,2) dupa ce:
# a) a fost marit triunghi ABC de 2 ori dim normala
# b) a fost micit de 2 ori

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(1)

# Coordonatele triunghiului
A = (0, 0)
B = (1, 1)
C = (5, 2)

# Factorii de scalare
factor_mare = 2  # pentru mărire
factor_mic = 0.5  # pentru micșorare (1/2)

# Functii pentru scalare
def scalare(punct, factor):
    x, y = punct
    x_prime = x * factor
    y_prime = y * factor
    return (x_prime, y_prime)

A_mare = scalare(A, factor_mare)
B_mare = scalare(B, factor_mare)
C_mare = scalare(C, factor_mare)

A_mic = scalare(A, factor_mic)
B_mic = scalare(B, factor_mic)
C_mic = scalare(C, factor_mic)

def deseneaza_triunghi(p1, p2, p3, contur, umplere):
    pen.penup()
    pen.goto(p1[0] * 50 - 100, p1[1] * 50)
    pen.color(contur, umplere)
    pen.begin_fill()
    pen.pendown()
    pen.goto(p2[0] * 50 - 100, p2[1] * 50)
    pen.goto(p3[0] * 50 - 100, p3[1] * 50)
    pen.goto(p1[0] * 50 - 100, p1[1] * 50)
    pen.end_fill()

# Desenăm triunghiul inițial
deseneaza_triunghi(A, B, C, "blue", "lightblue")

# Desenăm triunghiul mărit
deseneaza_triunghi((A_mare[0], A_mare[1] - 3), (B_mare[0], B_mare[1] - 3), (C_mare[0], C_mare[1] - 3), "red", "yellow")

# Desenăm triunghiul micșorat
deseneaza_triunghi((A_mic[0], A_mic[1] - 6), (B_mic[0], B_mic[1] - 6), (C_mic[0], C_mic[1] - 6), "green", "orange")

pen.hideturtle()
screen.exitonclick()

