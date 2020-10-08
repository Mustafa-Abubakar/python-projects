import pygame, sys
from pygame.locals import *
pygame.init()

# set up the window
display = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Hello")

music = pygame.mixer.music.load('tetrisc.mid')
pygame.mixer.music.play(-1, 0.0)

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 128)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()