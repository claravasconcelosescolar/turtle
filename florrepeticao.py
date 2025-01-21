import turtle

esguicho = turtle.Turtle()

for i in range(12):
    for _ in range(2):
        esguicho.forward(60)
        esguicho.left(30)
        esguicho.forward(60)
        esguicho.left(150)
    esguicho.left(30)

turtle.done()