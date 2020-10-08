import pygame, sys
from pygame.locals import *
pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("drawing")

# set uo the colors
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# draw the surface object
display.fill(WHITE)
pygame.draw.polygon(display, GREEN, ((140, 0), (291, 106),(236, 277), (56, 277), (0, 106) ))
pygame.draw.line(display, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(display, BLUE, (120, 60), (60, 120))
pygame.draw.line(display, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(display, BLUE, (300, 50), 50, 0)
pygame.draw.ellipse(display, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(display, RED, (200, 150, 100, 50))

pixobject = pygame.PixelArray(display)
pixobject[480][380] = BLACK
pixobject[482][382] = BLACK
pixobject[484][384] = BLACK
pixobject[486][386] = BLACK
pixobject[488][388] = BLACK
del pixobject



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()