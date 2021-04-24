def Polygone(sides, long):
    from turtle import Turtle, Screen
    t = Turtle()
    s = Screen()
    angle = (sides-2)*90/sides
    for i in range(sides):
        t.forward(long)
        t.left(angle)
