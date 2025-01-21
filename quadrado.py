import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("purple")

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.exitonclick()

