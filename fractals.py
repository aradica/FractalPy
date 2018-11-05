#import numpy as np
#from matplotlib import pyplot as plt
import turtle as tt

def drawTriangle(x, y, pen, a):
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()
    for i in range(3):
        pen.forward(a)
        pen.left(120)

def drawNgon(x, y, pen, a, N, rot):
    vertices = []
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()
    pen.setheading(rot)

    phi = 360/N
    for i in range(N):
        pen.forward(a)
        pen.left(phi)
        vertices.append((pen.xcor(), pen.ycor()))

    return vertices
def drawStep(x, y, pen, a):
    #parent
    drawTriangle(x, y, pen, a)

    #children
    drawTriangle(x, y, pen, a/2)
    drawTriangle(a/2+x, y, pen, a/2)
    drawTriangle(a/4+x, (3**0.5)*a/4+y, pen, a/2)



def drawST(x, y, pen, a, steps):
    if steps > 0:

        coordinates  = []
        drawStep(x, y, pen, a)
        coordinates.append((x, y))
        coordinates.append((a/2+x, y))
        coordinates.append((a/4+x, (3**0.5)*a/4+y))

        a = a/2

        for x, y in coordinates:
            drawStep(x, y, pen, a)

        for x, y in coordinates:
            drawST(x, y, pen, a, steps-1)



window = tt.Screen()
pen = tt.Turtle()
pen.speed(10)
#drawST(-100, -100, pen, 500, 3)


rot = 360/5
pentagon = drawNgon(0, 0, pen, 100, 5, 0)
for x,y in pentagon:
    drawNgon(x, y, pen, 100, 5, rot)


window.exitonclick()

#TODO: 3D!!!