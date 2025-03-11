import turtle
turtle.Screen().bgcolor("black")
window=turtle.Screen()
window.setup(400,400)
turtle.title("Rainbow Spiral")
rainbow=turtle.Turtle()
num_colors = ["red","yellow","blue","violet","orange","green", "indigo"]
while True:
    for i in range(200):
        rainbow.pencolor(num_colors[i%len(num_colors)])
        rainbow.forward(i)
        rainbow.left(20)
turtle.done()