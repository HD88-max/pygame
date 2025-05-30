import pygame
pygame.init()
x,y = 400,400
current_colour=pygame.Color("red")
screen = pygame.display.set_mode((800,800))
playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = pygame.quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                x = x- 10
                current_colour=pygame.Color("blue")
            if e.key == pygame.K_RIGHT:
                x = x + 10
                current_colour=pygame.Color("green")
            if e.key == pygame.K_UP:
                y = y -10
                current_colour=pygame.Color("purple")
            if e.key == pygame.K_DOWN:
                y = y + 10
                current_colour=pygame.Color("yellow")
    screen.fill((0,0,0))
    pygame.draw.circle(screen,current_colour,(x,y),200)
    pygame.display.flip()
