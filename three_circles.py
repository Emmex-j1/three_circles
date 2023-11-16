import turtle 

screen = turtle.Screen()
screen.bgcolor("white")
circle = turtle.Turtle()

radii = [50, 100 ,150]
color = ['red', 'green', 'blue']

for radius, color in zip(radii, color):
    circle.fillcolor(color)
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()
    circle.penup()
    circle.goto(0, -radius-50)
    circle.pendown()


circle.hideturtle()
turtle.done()