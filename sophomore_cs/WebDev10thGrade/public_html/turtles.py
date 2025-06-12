import turtle

raphael = turtle.Turtle()


def snowflake(y,order,size):
    setxy(y,-250,150)
    koch(y,order,size)
    y.right(120)
    koch(y,order,size)
    y.right(120)
    koch(y,order,size)

snowflake(t,3,500)
window = turtle.Screen()
window.exitonclick()
