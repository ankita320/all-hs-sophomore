import turtle


def hexspin(drawer, size, levels):
    turtle.bgcolor("#40E0D0")
    drawer.width(2)
    if levels == 0:
        drawer.forward(size)
    else:
        colors = ['red', '#CF9FFF', '#6495ED', '#FF00FF', 'orange', '#DFFF00']
        drawer.pencolor(colors[int(1)])
        drawer.fillcolor("#9cedfb")
        drawer.begin_fill()
        hexspin(drawer, size/2.0, levels-1)
        drawer.right(60)
        drawer.pencolor(colors[int(2)])
        hexspin(drawer, size/2.0, levels-1)
        drawer.right(60)
        hexspin(drawer, size/2.0, levels-1)
        drawer.right(60)
        drawer.pencolor(colors[int(3)])
        hexspin(drawer, size/2.0, levels-1)
        drawer.right(60)
        drawer.pencolor(colors[int(4)])
        hexspin(drawer, size/2.0, levels-1)
        drawer.left(60)
        drawer.pencolor(colors[int(5)])
        hexspin(drawer, size/2.0, levels-1)
        drawer.right(60)
        drawer.end_fill()
        drawer.hideturtle()
 
           
spin = turtle.Turtle()
spin.speed(0)
spin.penup()
spin.goto(-150,-100)
spin.pendown()

hexspin(spin, 200, 3)
hexspin(spin, 200, 3)
window = turtle.Screen()
window.exitonclick()
