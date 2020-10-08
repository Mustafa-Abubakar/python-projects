import pygame

win = pygame.display.set_mode((1000,570))
pygame.display.set_caption("Penalty Score")

bg = pygame.image.load('D:\Python\images\stadium1.jpg')
goal =  pygame.image.load('D:\Python\images\goal.png')
goalkeeper = pygame.image.load('D:\Python\images\goalkeeper1.png')
def design():
    win.blit(bg, (0, 0))
    win.blit(goal, (200,-40))
    #win.blit(goalkeeper, (-100,-10))
    pygame.draw.circle(win, (255, 0, 0),(500, 250),50)
    pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    design()

pygame.quit()
