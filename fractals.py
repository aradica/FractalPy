import turtle as tt

def setPen(pen, x, y, heading=None):
    """
    Place the Turtle() at a certain x and y.
    If heading==None then it remains what it was before
    """
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()
    if heading != None:
        pen.setheading(heading)

def drawTriangle(pen, edge):
    """
    Draws a triangle, takes edge size for input
    Use with setPen() to choose location and rotation
    """
    for k in range(3):
        pen.forward(edge)
        pen.left(120)


class Ngon:
    """
    A general class for Ngons
    """
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
        """
        Draw the Ngon with a Turtle() object
        """

        setPen(self.x, self.y, self.rotation)
        pen.begin_poly()
        for i in range(self.n):
            pen.forward(self.edge)
            pen.left(self.phi)
        pen.end_poly()

        self.vertices = pen.get_poly()

class SierpinskiTriangle:
    """
    edge: the largest vertice
    iterations: 'depth'
    x, y, rotation - optional coordinate system parameters
    """
    def __init__(self, edge, iterations, x=0, y=0, rotation=0):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.edge = edge
        self.iterations = iterations

        self.generations = self._makeGenerations()


    def _makeGenerations(self):
        return [Ngon(self.edge/(2**i), 3) for i in range(self.iterations)]


    def drawGeneration(self, i, x, y, pen):
        """
        Draws the i-th generation with a Turtle() object
        """
        setPen(pen, x, y, self.rotation)

        pen.begin_poly()
        drawTriangle(pen, self.generations[i].edge)
        pen.end_poly()
        vertices = pen.get_poly()
        x1, y1 = vertices[1]
        setPen(pen, x1, y1, self.rotation)      
        drawTriangle(pen, self.generations[i].edge)

        x2, y2 = vertices[2]
        setPen(pen, x2, y2, self.rotation)
        drawTriangle(pen, self.generations[i].edge)

        return [(x, y), (x1, y1), (x2, y2)]
    

    def drawAll(self, pen, iteration=0, g=None):
        """
        Draw the entire Sierpinski triangle
        iteration and g variables should be left at their default states!
        """
        print("Working on iteration:", iteration)
        if iteration == 0:
            g = self.drawGeneration(iteration, self.x, self.y, pen)
            self.drawAll(pen, iteration+1, g)

        else:
            if iteration < self.iterations:
                for k in g:
                    g2 = self.drawGeneration(iteration, k[0], k[1], pen)
                    self.drawAll(pen, iteration+1, g2)


if __name__ == "__main__":
    window = tt.Screen()
    pen = tt.Turtle()
    pen.speed(100)

    A = 200
    ITERS = 5
    X, Y = -150, -150
    x = SierpinskiTriangle(A, ITERS, X, Y)
    x.drawAll(pen)
    print(x.generations)
    window.exitonclick()
