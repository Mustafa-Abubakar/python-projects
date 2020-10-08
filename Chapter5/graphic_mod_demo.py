import turtle
import my_graphic

X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50


def main():
    turtle.hideturtle()

    # draw a square
    my_graphic.square(X2, Y2, (X3-X2), "gray")


    # draw a circle
    my_graphic.circle(X1, Y1, RADIUS, "blue")
    my_graphic.circle(X2, Y2, RADIUS, "red")
    my_graphic.circle(X3, Y3, RADIUS, "green")

    # draw a line
    my_graphic.line(X1, Y1, X2, Y2, "black")
    my_graphic.line(X1, Y1, X3, Y3, "black")
    my_graphic.line(X2, Y2, X3, Y3, "black")
    
    turtle.done()


main()
