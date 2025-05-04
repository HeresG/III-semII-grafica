import pygame

pygame.init()
window = pygame.display.set_mode([800,600])

# X and Y represent the position where the rectangle will be displayed

color= [0,0,255]
positions = [(0,0),(25,50),(10,100),(10,50)]
pygame.draw.polygon(window, color, positions)


pygame.display.flip()

run = True

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
pygame.quit()
exit()