import turtle as tt

def setPen(x, y, rotation):
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()
    pen.setheading(rotation)

def drawTriangle(edge):
    for k in range(3):
        pen.forward(edge)
        pen.left(120)


class Ngon:
    def __init__(self, edge, n, x=0, y=0, rotation=0):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.edge = edge
        self.n = n
        self.phi = 360/n
        self.vertices = None

    def __repr__(self):
        return "Ngon object with {} vertices of size {}".format(self.n, self.edge)

    def draw(self, pen):
        pen.penup()
        pen.setx(self.x)
        pen.sety(self.y)
        pen.pendown()
        pen.setheading(self.rotation)

        pen.begin_poly()
        for i in range(self.n):
            pen.forward(self.edge)
            pen.left(self.phi)

        self.vertices = pen.get_poly()

class SierpinskiTriangle:
    def __init__(self, edge, iterations, x=0, y=0, rotation=0):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.edge = edge
        self.iterations = iterations

        self.generations = None


    def makeGenerations(self):
        self.generations = [Ngon(self.edge/(2**i), 3) for i in range(self.iterations)]


    def drawGeneration(self, i, x, y, pen):
        setPen(x, y, self.rotation)

        pen.begin_poly()
        drawTriangle(self.generations[i].edge)
        vertices = pen.get_poly()
        x1, y1 = vertices[1]
        setPen(x1, y1, self.rotation)      
        drawTriangle(self.generations[i].edge)

        x2, y2 = vertices[2]
        setPen(x2, y2, self.rotation)
        drawTriangle(self.generations[i].edge)

        return [(x, y), (x1, y1), (x2, y2)]
    

    def drawAll(self, pen, iteration=0, g=None):
        print("Working on iteration:", iteration)
        if iteration == 0:
            g = self.drawGeneration(iteration, self.x, self.y, pen)
            self.drawAll(pen, iteration+1, g)

        else:
            if iteration < self.iterations:
                for k in g:
                    g2 = self.drawGeneration(iteration, k[0], k[1], pen)
                    self.drawAll(pen, iteration+1, g2)





window = tt.Screen()
pen = tt.Turtle()
pen.speed(100)
x = SierpinskiTriangle(200, 5, -100, -100)
x.makeGenerations()
#x.drawGeneration(0, 0, 0, pen)
x.drawAll(pen)
print(x.generations)

window.exitonclick()
