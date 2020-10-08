import pygame # importing pygame
pygame.init() # initialazing pygame
win = pygame.display.set_mode((500,480)) # seting up pygame window
pygame.display.set_caption("My first Game") # pygame window title

walkRight = [pygame.image.load("files\R1.png"), pygame.image.load("files\R2.png"), pygame.image.load("files\R3.png"), pygame.image.load("files\R4.png"), pygame.image.load("files\R5.png"), pygame.image.load("files\R6.png"), pygame.image.load("files\R7.png"), pygame.image.load("files\R8.png"), pygame.image.load("files\R9.png")]
walkLeft = [pygame.image.load('files\L1.png'), pygame.image.load('files\L2.png'), pygame.image.load('files\L3.png'), pygame.image.load('files\L4.png'), pygame.image.load('files\L5.png'), pygame.image.load('files\L6.png'), pygame.image.load('files\L7.png'), pygame.image.load('files\L8.png'), pygame.image.load('files\L9.png')]
char = pygame.image.load('files\standing.png')
bg = pygame.image.load('files\pg.jpg')

Clock = pygame.time.Clock()


x = 50
y = 400
height = 64
width = 64
velocity = 5

isJump = False
JumpCount = 10
left = False
right = False
walkCount = 0

radius = 0
color = ''
facing = 0


def draw():
    global x, y, velocity, color, facing
    velocity = 8 * facing
    pygame.draw.circle(win, color, (x, y), radius)

# moving function and controlling the bodieries
def move():
    global x, y, isJump, JumpCount, left, right, walkCount
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >velocity :
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - velocity:
        x += velocity
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left =  False
            right = False
            walkCount = 0
    else:
        if JumpCount >= -10:
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount ** 2) * 0.5 * neg
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10

# function that draws on the window
def redRowGemeWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

# pygame main loop
running = True
while running:
    Clock.tick(27)
    # checking the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calling draw function
    redRowGemeWindow()
    # moving
    move()



pygame.quit()
