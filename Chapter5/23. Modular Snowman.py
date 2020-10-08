import turtle

def main():
    drawBase(0,0,100,"red")
    drawMidSection(0,155,60,"blue")
    drawArms(-30,185, 30, 185)
    turtle.hideturtle()
    turtle.done()
def drawBase(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def drawMidSection(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def drawArms(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(50)
    turtle.setheading(100)
    turtle.forward(45)
    turtle.setheading(95)
    turtle.forward(5)
    turtle.backward(5)
    turtle.setheading(105)
    turtle.forward(5)

    turtle.penup()
    turtle.setheading(40)
    turtle.pendown()
    turtle.forward(45)
    turtle.setheading(35)
    turtle.forward(5)
    turtle.backward(5)
    turtle.setheading(45)
    turtle.forward(5)


main()



