#Folosind Pygame in Python, Creeați Space Invaders plecand de la schita:
#a. [20p] Jucator: poate sa se deplaseze stanga(A) / dreapta(D) si sa lanseze proiecƟle (Space)
#b. [20p] Bunkere destrucƟbile
#c. [20p] Inamici mobili organizaƟ in 5 randuri
#d. [20p] Cel mai apropiat inamic de pe fiecare coloana ataca
#e. [20p] Score si High-Score (salvat intre run-uri


import pygame
import sys
import random
import os

# Inițializare Pygame
pygame.init()

# Setări ecran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Culori
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Fișier pentru highscore
HS_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HS_FILE):
        with open(HS_FILE, "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    with open(HS_FILE, "w") as f:
        f.write(str(score))

highscore = load_highscore()

# Jucător
player_width, player_height = 50, 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 5

# Proiectile jucător
player_bullets = []
bullet_speed = 7
max_player_bullets = 3

# Bunkere
bunker_width, bunker_height = 80, 40
bunker_count = 4
bunkers = []

for i in range(bunker_count):
    x = 100 + i * 150
    y = HEIGHT - 150
    bunkers.append(pygame.Rect(x, y, bunker_width, bunker_height))

# Inamici
enemy_rows = 5
enemy_cols = 10
enemy_width, enemy_height = 40, 30
enemy_x_start = 50
enemy_y_start = 50
enemy_x_spacing = 60
enemy_y_spacing = 50
enemy_speed = 1
enemy_direction = 1  # 1 = dreapta, -1 = stânga

enemies = []
for row in range(enemy_rows):
    for col in range(enemy_cols):
        x = enemy_x_start + col * enemy_x_spacing
        y = enemy_y_start + row * enemy_y_spacing
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Proiectile inamici
enemy_bullets = []
enemy_bullet_speed = 5
enemy_shoot_interval = 1000  # ms
last_enemy_shot = pygame.time.get_ticks()

# Scor
score = 0

def draw_player():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

def draw_bunkers():
    for bunker in bunkers:
        pygame.draw.rect(screen, BLUE, bunker)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def draw_bullets():
    for b in player_bullets:
        pygame.draw.rect(screen, WHITE, b)
    for b in enemy_bullets:
        pygame.draw.rect(screen, RED, b)

def move_enemies():
    global enemy_direction, enemy_speed, enemies
    edge_reached = False
    for enemy in enemies:
        enemy.x += enemy_speed * enemy_direction
        if enemy.right >= WIDTH - 10 or enemy.left <= 10:
            edge_reached = True
    if edge_reached:
        enemy_direction *= -1
        for enemy in enemies:
            enemy.y += 10  # coboară un pas

def handle_player_input(keys):
    global player_x
    if keys[pygame.K_a]:
        player_x -= player_speed
        if player_x < 0:
            player_x = 0
    if keys[pygame.K_d]:
        player_x += player_speed
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width

def update_bullets():
    global score
    # Proiectile jucator
    for bullet in player_bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            player_bullets.remove(bullet)
        else:
            # Verifică coliziuni cu inamici
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    if bullet in player_bullets:
                        player_bullets.remove(bullet)
                    score += 10
                    break
            # Verifică coliziuni cu bunkere
            for bunker in bunkers[:]:
                if bullet.colliderect(bunker):
                    bunkers.remove(bunker)
                    if bullet in player_bullets:
                        player_bullets.remove(bullet)
                    break

    # Proiectile inamici
    for bullet in enemy_bullets[:]:
        bullet.y += enemy_bullet_speed
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)
        else:
            # Verifică coliziuni cu bunkere
            for bunker in bunkers[:]:
                if bullet.colliderect(bunker):
                    bunkers.remove(bunker)
                    if bullet in enemy_bullets:
                        enemy_bullets.remove(bullet)
                    break
            # Verifică coliziune cu jucătorul
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            if bullet.colliderect(player_rect):
                # Termina jocul
                game_over()

def enemy_shoot():
    global last_enemy_shot
    now = pygame.time.get_ticks()
    if now - last_enemy_shot < enemy_shoot_interval:
        return
    # Pentru fiecare coloană găsim cel mai jos inamic (max y)
    cols = {}
    for enemy in enemies:
        col_index = (enemy.x - enemy_x_start) // enemy_x_spacing
        if col_index not in cols or enemy.y > cols[col_index].y:
            cols[col_index] = enemy
    # Inamici care trag
    for enemy in cols.values():
        bullet = pygame.Rect(enemy.centerx - 3, enemy.bottom, 6, 12)
        enemy_bullets.append(bullet)
    last_enemy_shot = now

def draw_score():
    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (10, 10))
    hs_surf = font.render(f"High Score: {highscore}", True, WHITE)
    screen.blit(hs_surf, (WIDTH - 200, 10))

def game_over():
    global highscore, score
    if score > highscore:
        highscore = score
        save_highscore(highscore)

    # Afișare mesaj
    screen.fill(BLACK)
    msg1 = font.render("Game Over!", True, RED)
    msg2 = font.render(f"Your score: {score}", True, WHITE)
    msg3 = font.render(f"High score: {highscore}", True, WHITE)
    screen.blit(msg1, (WIDTH//2 - msg1.get_width()//2, HEIGHT//2 - 60))
    screen.blit(msg2, (WIDTH//2 - msg2.get_width()//2, HEIGHT//2))
    screen.blit(msg3, (WIDTH//2 - msg3.get_width()//2, HEIGHT//2 + 40))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

# Bucla principală
running = True
while running:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Trage un glonț dacă nu există prea multe pe ecran
                if len(player_bullets) < max_player_bullets:
                    bullet = pygame.Rect(player_x + player_width//2 - 3, player_y, 6, 12)
                    player_bullets.append(bullet)

    keys = pygame.key.get_pressed()
    handle_player_input(keys)

    move_enemies()
    update_bullets()
    enemy_shoot()

    # Verifică dacă inamicii au ajuns prea jos → Game Over
    for enemy in enemies:
        if enemy.bottom >= player_y:
            game_over()

    # Dacă nu mai sunt inamici → câștigi și jocul se termină
    if not enemies:
        screen.fill(BLACK)
        win_msg = font.render("You Win!", True, GREEN)
        screen.blit(win_msg, (WIDTH//2 - win_msg.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False

    screen.fill(BLACK)
    draw_player()
    draw_bunkers()
    draw_enemies()
    draw_bullets()
    draw_score()

    pygame.display.flip()

pygame.quit()