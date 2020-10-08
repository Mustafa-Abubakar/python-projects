import pygame
import random

width = 360
height = 480
FPS = 30

# set up the colors
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


# initialize pygame and creat a window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
Clock = pygame.time.Clock()


# Game loop
running = True
while True:
    # process input(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # update
    # draw / render
    screen.fill(WHITE)
    # after drawing everything flip the display
    pygame.display.flip()
pygame.quit()