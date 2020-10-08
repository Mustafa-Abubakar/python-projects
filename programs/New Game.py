
import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0


# set up screen
wn = turtle.Screen()
wn.title("New Game @ Ascad Bin Abubakar")
wn.onkey(high_score,score)
wn.bgcolor("orchid")
wn.setup(width=700, height=600)
wn.tracer(0)

Player = turtle.Turtle()
Player.speed(0)
Player.settiltangle(90)
Player.shape("turtle")
Player.shapesize(3,3,3)
Player.color("black")
Player.penup()
Player.goto(0, -250)
Player.direction = "stop"

# Box drops
Drop1 = turtle.Turtle()
Drop1.speed(0)
Drop1.settiltangle(270)
#Drop1.shape("turtle")
Drop1.shapesize(1,1,3)
Drop1.color("blue")
Drop1.penup()
Drop1.goto(0, 400)
Drop1.direction = "down"

Drop2 = turtle.Turtle()
Drop2.speed(0)
Drop2.settiltangle(270)
#Drop2.shape("turtle")
Drop2.shapesize(1,1,3)
Drop2.color("yellow")
Drop2.penup()
Drop2.goto(-200, 600)
Drop2.direction = "down"

Drop3 = turtle.Turtle()
Drop3.speed(0)
Drop3.settiltangle(270)
#Drop3.shape("turtle")
Drop3.shapesize(1,1,3)
Drop3.color("powder blue")
Drop3.penup()
Drop3.goto(250, 700)
Drop3.direction = "down"

Drop4 = turtle.Turtle()
Drop4.speed(0)
Drop4.settiltangle(270)
#Drop4.shape("turtle")
Drop4.shapesize(1,1,3)
Drop4.color("brown")
Drop4.penup()
Drop4.goto(-250, 700)
Drop4.direction = "down"

Drop5 = turtle.Turtle()
Drop5.speed(0)
Drop5.settiltangle(270)
#Drop5.shape("turtle")
Drop5.shapesize(1,1,3)
Drop5.color("black")
Drop5.penup()
Drop5.goto(-250, 700)
Drop5.direction = "down"


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,275)
pen.write("Score : 0 \t\t\t\t\t  High Score: 0", align='center', font=("Courior",16,"normal"))


# Function of player
def go_up():
    Player.direction = "up"

def go_down():
    Player.direction = "down"

def go_right():
    Player.direction = "right"


def go_left():
    Player.direction = "left"



def move():
    if Player.direction == "up":
        y = Player.ycor()
        Player.sety(y+25)

    if Player.direction == "down":
        y = Player.ycor()
        Player.sety(y - 25)

    if Player.direction == "right":
        x = Player.xcor()
        Player.setx(x+25)

    if Player.direction == "left":
        x = Player.xcor()
        Player.setx(x-25)


# Function of Drops
def moveDrop1():
    y = Drop1.ycor()
    Drop1.sety(y - 15)

def moveDrop2():
    y = Drop2.ycor()
    Drop2.sety(y - 15)

def moveDrop3():
    y = Drop3.ycor()
    Drop3.sety(y - 15)

def moveDrop4():
    y = Drop4.ycor()
    Drop4.sety(y - 15)

def moveDrop5():
    y = Drop5.ycor()
    Drop5.sety(y - 15)

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

#main Game loop
while True:
    wn.update()

    # Check if the Drop
    if Drop1.ycor() < -300:
        x = random.randint(-300, 300)
        y = random.randint(400, 400)
        Drop1.goto(x, y)
        Drop1.direction = "down"

        # Shorted the delay
        delay -= 0.0001

        # Increase the score
        score += 2

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} \t\t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))

    if Drop2.ycor() < -300:
        x = random.randint(-350, 350)
        y = random.randint(400, 400)
        Drop2.goto(x, y)
        Drop2.direction = "down"

        # Shorted the delay
        delay -= 0.0001

        # Increase the score
        score += 2

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} \t\t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))

    if Drop3.ycor() < -300:
        x = random.randint(-350, 350)
        y = random.randint(400, 400)
        Drop3.goto(x, y)
        Drop3.direction = "down"

        # Shorted the delay
        delay -= 0.0001

        # Increase the score
        score += 2

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} \t\t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))

    if Drop4.ycor() < -300:
        x = random.randint(-350, 350)
        y = random.randint(400, 400)
        Drop4.goto(x, y)
        Drop4.direction = "down"

        # Shorted the delay
        delay -= 0.0001

        # Increase the score
        score += 4

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} \t\t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))

    if Drop5.ycor() < -300:
        x = random.randint(-350, 350)
        y = random.randint(400, 400)
        Drop5.goto(x, y)
        Drop5.direction = "down"

        # Shorted the delay
        delay -= 0.0001

        # Increase the score
        score += 2

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} \t\t\t\t High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))


    # Check for a collison with the border
    if Player.xcor() > 300 or Player.xcor() < -300 or Player.ycor() > 250 or Player.ycor() < -250:
        time.sleep(1)
        Player.goto(0, -250)
        Player.direction = "stop"
        Drop1.goto(0,400)
        Drop2.goto(-200,600)
        Drop3.goto(20, 700)
        Drop4.goto(-250, 700)
        Drop5.goto(-250, 700)

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the screen display
        pen.clear()
        pen.write("Score : {} \t\t\t\t  High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))


    # Check for a collison with the drop
    if (Player.distance(Drop1) <= 30 or Player.distance(Drop2) <= 30 or Player.distance(Drop3) <= 30
        or Player.distance(Drop4) <= 30 or Player.distance(Drop5) <= 30):
        time.sleep(1)
        Player.goto(0, -250)
        Player.direction = "stop"
        Drop1.goto(0, 400)
        Drop2.goto(-200, 600)
        Drop3.goto(20, 700)
        Drop4.goto(-250, 700)
        Drop5.goto(-250, 700)

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the screen display
        pen.clear()
        pen.write("Score : {} \t\t\t\t  High Score: {}".format(score, high_score), align='center',
                  font=("Courior", 16, "normal"))

    move()

    moveDrop1()
    moveDrop2()
    moveDrop3()
    moveDrop4()
    moveDrop5()


    time.sleep(delay)

wn.mainloop()
