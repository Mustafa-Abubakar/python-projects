import turtle
turtle.title("Star")
turtle.hideturtle()
turtle.penup()
turtle.goto(-150,0)
turtle.color("black","cyan")
turtle.begin_fill()
turtle.pendown()
for i in range(8):
    turtle.forward(300)
    turtle.left(135)
turtle.end_fill()
turtle.done()