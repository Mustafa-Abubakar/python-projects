import pygame, sys
from pygame.locals import *
pygame.init()

FBS = 30
fbsClock = pygame.time.Clock()

# set up the window
display = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catX = 10
catY = 10

direction = 'right'

while True:
    display.fill(WHITE)


    if direction == 'right':
        catX += 5
        if catX == 280:
            direction = 'down'

    elif direction == 'down':
        catX += 5
        if catX == 220:
            direction = 'left'

    elif direction == 'left':
        catX -= 5
        if catX == 10:
            direction = 'up'

    elif direction == 'up':
        catX -= 5
        if catX == 10:
            direction = 'right'

    display.blit(catImg, (catX, catY))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()