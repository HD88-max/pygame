# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.

import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(120,320,100,50))
    pygame.display.flip()