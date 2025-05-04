
import pygame
import sys
import math

pygame.init()

# Constants
width, height = 400, 400
background_color = (255, 255, 255)
blade_color = (0, 0, 0)
mill_color = (150, 150, 150)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Windmill")

# Windmill parameters
mill_x, mill_y = width // 2, height // 2
mill_size = 50
blade_length = 50
blade_width = 5
rotation_speed = 0.02

# Main game loop
angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(background_color)

    # Draw the windmill
    pygame.draw.rect(screen, mill_color, (mill_x - mill_size // 2, mill_y - mill_size // 2, mill_size, mill_size))
    
    # Calculate blade positions
    blade_x = mill_x + blade_length * math.cos(angle)
    blade_y = mill_y + blade_length * math.sin(angle)

    # Draw the rotating blade
    pygame.draw.line(screen, blade_color, (mill_x, mill_y), (blade_x, blade_y), blade_width)

    # Rotate the blade
    angle += rotation_speed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)