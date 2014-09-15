import turtle
from core.scene import Scene
from shapes.sphere import Sphere


def toto():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.circle(40, steps=4)  # Draw a square

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(40, steps=5)  # Draw a pentagon

    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.circle(40, steps=6)  # Draw a hexagon

    turtle.penup()
    turtle.goto(200, -50)
    turtle.pendown()
    turtle.circle(40)  # Draw a circle

    turtle.done()
    turtle.circle(50, steps=4)
    turtle.circle(40, steps=3)
    turtle.pendown()
    turtle.goto(-200, -50)
    turtle.penup()


def render2():
    my_scene = Scene()

    form1 = Sphere()
    my_scene.add_geometry(form1)
    my_scene.render()

def main():
    render2()

# toto()
if __name__ == '__main__':
    main()
