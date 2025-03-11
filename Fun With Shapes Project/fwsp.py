import turtle

def draw_polygon(sides, length, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)
    turtle.end_fill()

def main():
    turtle.bgcolor("lightblue")
    turtle.speed(3)
    
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    draw_polygon(3, 100, "red")
    
    turtle.penup()
    turtle.goto(50, 100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("green")
    for _ in range(2):
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    draw_polygon(6, 80, "blue")
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
