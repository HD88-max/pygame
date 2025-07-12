import pygame
import random
pygame.init()

screen=pygame.display.set_mode((800,600))
running = True

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("ufo.png"))

background = pygame.image.load("background.png")

playerimg= pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
def player(x,y):
    screen.blit(playerimg, (x, y))

enemyimg= pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
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

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 730:  # Assuming the width of the enemy image is 64
        enemyX_change = -0.3
        enemyY += enemyY_change

    screen.fill((255, 0, 0))  # Fill the screen with black
    screen.blit(background, (0, 0))  # Draw the background
    player(playerX, playerY)  # Call the player function to draw the spaceship
    enemy(enemyX, enemyY)  # Call the enemy function to draw the enemy
    pygame.display.update()
    