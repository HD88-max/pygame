# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0,125,255),(400,400),250, 20)
    pygame.draw.circle(screen,(0,125,255),(400,400),200)
    pygame.display.flip()
