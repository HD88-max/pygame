import pygame
import random
import math
pygame.init()

Screen_width = 800
Screen_height = 600
player_start_x = 370

screen=pygame.display.set_mode((Screen_width,Screen_height))
running = True

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("ufo.png"))

background = pygame.image.load("backround.png")

playerimg= pygame.image.load("spaceship.png")
playerX = player_start_x
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerimg, (x, y))

bulletimg= pygame.image.load("bullet.png")
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10)) 

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < 27  # Assuming the radius of the collision area is 27 pixels
enemyimg= []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6


for _i in range(no_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change = 0.3
    enemyY_change = 40


def enemy(x,y):
    screen.blit(enemyimg, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:  # Assuming the width of the screen is 800
        playerX = 730

    for i in range(no_of_enemies):
        enemyX[i] += enemyX_change
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:  # Assuming the width of the enemy image is 64
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            pass  


        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = playerY
            bullet_state = "ready"
            print("Collision detected")
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
    screen.fill((255, 0, 0))  # Fill the screen with black
    screen.blit(background, (0, 0))  # Draw the background
    player(playerX, playerY)  # Call the player function to draw the spaceship
    enemy(enemyX, enemyY)  # Call the enemy function to draw the enemy
    pygame.display.update()
    