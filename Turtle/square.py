import turtle
turtle.Screen().bgcolor("orange")
window=turtle.Screen()
window.setup(400,400)
turtle.title("Welcome to Turtle Window")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)

turtle.done()