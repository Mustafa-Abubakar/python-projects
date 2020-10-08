import turtle
screen_width = 600
screen_height = 600
target_left_x = 100
target_left_y = 250
target_width = 25
force_factor = 30
projectile_speed = 1
north = 90
south = 270
east = 0
west = 0
turtle.setup(screen_width,screen_height)
turtle.hideturtle()
turtle.penup()
turtle.speed(0)
turtle.goto(target_left_x,target_left_y)
turtle.pendown()
turtle.setheading(east)
turtle.forward(target_width)
turtle.setheading(north)
turtle.forward(target_width)
turtle.setheading(west)
turtle.forward(target_width)
turtle.setheading(south)
turtle.forward(target_width)
turtle.penup()
turtle.goto(0,0)
turtle.setheading(east)
turtle.speed(projectile_speed)
angle = float(input("Enter the projectile angle:  "))
force = float(input("Enter the launch force)(1-10): "))
distance = force * force_factor
turtle.setheading(angle)
turtle.penup()
turtle.forward(distance)
if (turtle.xcor() >= target_left_x and turtle.xcor() <= (target_left_x + target_width) and
    turtle.ycor() >= target_left_y and turtle.ycor() <= (target_left_y + target_width)):
    print("TARGET HIT! ")
else:
    print("YOU MISSED THE TARGET")