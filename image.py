# Write a program to create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.

import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
image = pygame.image.load("im.png")
background = pygame.transform.scale(image.convert(),[800,800])
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background,(0,0))