import turtle

esguicho = turtle.Turtle()

# definindo a função
def desenhe_uma_flor():
    for _ in range(6):
        for _ in range(8):
            esguicho.forward(20)
            esguicho.right(30)
        esguicho.right(60)

def pula (pixels):
    esguicho.penup()
    esguicho.forward(pixels)
    esguicho.pendown()

desenhe_uma_flor()
pula(150)
desenhe_uma_flor()
pula(150)
desenhe_uma_flor()