#Folosind Pygame in Python, trasati: 2 oameni de zapada statici, un fulg de nea rotitor si un avion
#in miscare.

import pygame
import math
import sys

# Inițializare
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tema 6 - Grafica: Oameni de zăpadă, fulg și avion")
clock = pygame.time.Clock()

# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)


# Fulg de nea
def draw_snowflake(center, angle):
    x, y = center
    r = 20
    for i in range(6):
        theta = angle + i * math.pi / 3
        x_end = x + r * math.cos(theta)
        y_end = y + r * math.sin(theta)
        pygame.draw.line(screen, WHITE, center, (x_end, y_end), 2)


# Om de zăpadă
def draw_snowman(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 30)  # cap
    pygame.draw.circle(screen, WHITE, (x, y + 40), 40)  # trunchi
    pygame.draw.circle(screen, WHITE, (x, y + 100), 50)  # bază
    pygame.draw.circle(screen, BLACK, (x - 10, y - 10), 3)  # ochi stâng
    pygame.draw.circle(screen, BLACK, (x + 10, y - 10), 3)  # ochi drept
    pygame.draw.polygon(screen, ORANGE, [(x, y), (x + 15, y + 5), (x, y + 5)])  # nas


# Avion
def draw_plane(x, y):
    # Corpul avionului
    pygame.draw.rect(screen, BLUE, (x - 40, y - 10, 60, 20))

    # Aripi
    pygame.draw.polygon(screen, BLUE, [(x - 10, y - 10), (x + 10, y - 30), (x + 20, y - 10)])  # aripa superioară
    pygame.draw.polygon(screen, BLUE, [(x - 10, y + 10), (x + 10, y + 30), (x + 20, y + 10)])  # aripa inferioară

    # Coada
    pygame.draw.polygon(screen, BLUE, [(x - 40, y - 10), (x - 60, y - 20), (x - 50, y)])  # coada stângă sus
    pygame.draw.polygon(screen, BLUE, [(x - 40, y + 10), (x - 60, y + 20), (x - 50, y)])  # coada stângă jos

    # Fereastră avion
    pygame.draw.circle(screen, WHITE, (x + 10, y), 5)


# Poziții inițiale
angle = 0
plane_x = -40
plane_y = 100

# Bucla principală
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 60))  # fundal albastru închis

    # Desenează 2 oameni de zăpadă
    draw_snowman(200, 350)
    draw_snowman(600, 350)

    # Fulg de nea rotativ
    draw_snowflake((400, 100), angle)
    angle += 0.05  # rotație continuă

    # Avion în mișcare
    draw_plane(plane_x, plane_y)
    plane_x += 2
    if plane_x > WIDTH + 60:
        plane_x = -60  # reapare din stânga

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
