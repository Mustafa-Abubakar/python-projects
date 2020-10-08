import turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed(60)
turtle.color("black","cyan")
turtle.begin_fill()
for x in range (36):
    turtle.forward(400)
    turtle.left(170)
turtle.end_fill()
turtle.done()
