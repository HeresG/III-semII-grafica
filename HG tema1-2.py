# Se cere translatia de vectori v=2i+2j a triunghiului ABC de varfuri A(1,2), B(5,6), C(-2,-1)
# NU MERGE CALUMEA
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(2)
pen.speed(1)

# Coordonate originale
A = (1, 2)
B = (5, 6)
C = (-2, -1)

# Vector de translație
vx, vy = 2, 2

# Coordonate translatate
A_t = (A[0] + vx, A[1] + vy)
B_t = (B[0] + vx, B[1] + vy)
C_t = (C[0] + vx, C[1] + vy)

scale = 40

def deseneaza_triunghi(p1, p2, p3, contur, umplere):
    pen.penup()
    pen.goto(p1[0]*scale, p1[1]*scale)
    pen.color(contur, umplere)
    pen.begin_fill()
    pen.pendown()
    pen.goto(p2[0]*scale, p2[1]*scale)
    pen.goto(p3[0]*scale, p3[1]*scale)
    pen.goto(p1[0]*scale, p1[1]*scale)
    pen.end_fill()

# triunghiul original
deseneaza_triunghi(A, B, C, "blue", "lightblue")

# triunghiul translatat
deseneaza_triunghi(A_t, B_t, C_t, "red", "pink")

def scrie_eticheta(punct, nume):
    pen.penup()
    pen.goto(punct[0]*scale + 5, punct[1]*scale + 5)
    pen.pendown()
    pen.write(nume, font=("Arial", 10, "normal"))

scrie_eticheta(A, "A")
scrie_eticheta(B, "B")
scrie_eticheta(C, "C")
scrie_eticheta(A_t, "A'")
scrie_eticheta(B_t, "B'")
scrie_eticheta(C_t, "C'")

pen.hideturtle()
screen.exitonclick()
