import turtle
import time
import random

delay = 0.2

#score
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
wn.title("New One @ Ascad Bin Abubakar")
wn.bgcolor("blue")
wn.setup(width=900, height=600)
wn.tracer(0)

#designing
w=turtle.Turtle()
w.penup()
w.goto(400,-300)
w.pendown()
w.fillcolor("powder blue")
w.begin_fill()
w.setheading(270)
w.forward(150)
w.setheading(180)
w.forward(1500)
w.setheading(90)
w.forward(150)
w.setheading(0)
for x in range(60):
    w.right(45)
    w.forward(30)
    w.left(105)
    w.forward(30)
    w.setheading(0)
w.end_fill()


#Player Setup
Player = turtle.Turtle()
Player.speed(0)
Player.settiltangle(90)
Player.shape("circle")
Player.shapesize(2,2,2)
Player.color("black")
Player.penup()
Player.goto(0, 300)
Player.direction = "stop"

# walls
wall1 = turtle.Turtle()
wall1.speed(0)
wall1.settiltangle(270)
wall1.shape("triangle")
wall1.shapesize(5,1,9)
wall1.color("purple")
wall1.penup()
wall1.goto(-370,0)
wall1.direction = "left"

wall2 = turtle.Turtle()
wall2.speed(0)
wall2.settiltangle(270)
wall2.shape("triangle")
wall2.shapesize(5,1,9)
wall2.color("purple")
wall2.penup()
wall2.goto(-180,-50)

wall3 = turtle.Turtle()
wall3.speed(0)
wall3.settiltangle(270)
wall3.shape("triangle")
wall3.shapesize(5,1,9)
wall3.color("purple")
wall3.penup()
wall3.goto(0,-100)

wall4 = turtle.Turtle()
wall4.speed(0)
wall4.settiltangle(270)
wall4.shape("triangle")
wall4.shapesize(5,1,9)
wall4.color("purple")
wall4.penup()
wall4.goto(190,-50)

wall5 = turtle.Turtle()
wall5.speed(0)
wall5.settiltangle(270)
wall5.shape("triangle")
wall5.shapesize(5,1,9)
wall5.color("purple")
wall5.penup()
wall5.goto(390,0)


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,275)
pen.write("Score : 0 \t\t\t\t\t\t  High Score: 0", align='center', font=("algerian",16,"normal"))


# Function of player
def moveply1():
   y = Player.ycor()
   Player.sety(y - 0.5)



def go_up():
    Player.direction = "up"

def go_right():
    Player.direction = "right"

def go_left():
    Player.direction = "left"


def move():
    if Player.direction == "up":
        y = Player.ycor()
        Player.sety(y + 200)
        Player.direction="stop"



    if Player.direction == "right":
        x = Player.xcor()
        Player.setx(x + 80)
        Player.direction = "stop"

    if Player.direction == "left":
        x = Player.xcor()
        Player.setx(x - 80)
        Player.direction="stop"


# Function of Drops
def movewall1():
    x = wall1.xcor()
    wall1.setx(x - 0.2)

def movewall2():
    x = wall2.xcor()
    wall2.setx(x - 0.2)

def movewall3():
    x = wall3.xcor()
    wall3.setx(x - 0.2)

def movewall4():
    x = wall4.xcor()
    wall4.setx(x - 0.2)

def movewall5():
    x = wall5.xcor()
    wall5.setx(x - 0.2)

def main():
    if not (Player.distance(wall1)<30 or Player.distance(wall2)<30 or Player.distance(wall3)<30 or
            Player.distance(wall4)<30 or Player.distance(wall5)<30):
        Player.direction=move()
        moveply1()






    move()
    movewall1()
    movewall2()
    movewall3()
    movewall4()
    movewall5()


# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# main game loop
while True:
    wn.update()

    if (Player.distance(wall1) < 30 or Player.distance(wall2) < 30 or Player.distance(wall3) < 30 or
            Player.distance(wall4) < 30 or Player.distance(wall5) < 30):
        #Shorted the delay
        delay -= 0.001

        # Increase the score
        #score += 2

        if score > high_score:
            high_score = score

        # pen.write("Score : {} \t\t\t\t\t\t  High Score: {}".format(score, high_score), align='center', font=("algerian", 16, "normal"))

    #check if the ball is fall in water or not
    if Player.ycor() < -150:
        time.sleep(1)
        Player.goto(0, 300)
        Player.direction = "down"
        wall1.goto(-370,0)
        wall2.goto(-180,-50)
        wall3.goto(0,-100)
        wall4.goto(190,-50)
        wall5.goto(390,0)

        # Reset the delay
        delay = 0.2

        # Reset the score
        score = 0

        # Update the screen display
        pen.clear()
        pen.write("Score : {} \t\t\t\t  High Score: {}".format(score, high_score), align='center',
                   font=("algerian", 16, "normal"))

    # Check walls
    if wall1.xcor() < -480:
        x = 500
        y = random.randint(-100, 50)
        wall1.goto(x, y)
        wall1.direction = "left"

    if wall2.xcor() < -480:
        x = 500
        y = random.randint(-100, 50)
        wall2.goto(x, y)
        wall2.direction = "left"

    if wall3.xcor() < -480:
        x = 500
        y = random.randint(-100, 50)
        wall3.goto(x, y)
        wall3.direction = "left"

    if wall4.xcor() < -480:
        x = 500
        y = random.randint(-100, 50)
        wall4.goto(x, y)
        wall4.direction = "left"

    if wall5.xcor() < -480:
        x = 500
        y = random.randint(-100, 50)
        wall5.goto(x, y)
        wall5.direction = "left"



    main()


wn.mainloop()