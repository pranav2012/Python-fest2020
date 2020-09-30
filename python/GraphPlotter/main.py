"""
====================
2D /3D Graph plotter
====================

Class TwoDGraph: for 2D line and scatter plot. 

Class ThreeDGraph: for 3D line, scatter and surface plot

"""


import numpy as np
from matplotlib import pyplot
from matplotlib import cm
from mpl_toolkits import mplot3d


# helper function
def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


class TwoDGraph:

    """
    Creating an object
        myObj = TwoDGraph(n, x, y, title, labeX, labelY)

    If you want to get userinput you can use the getUserInput class method. 
        myObj = TwoDGraph().getUserInput()

    Now if you want to plot 
    2-d Line Graph:
        myObj.plotLineGraph()

    2-d Scatter graph:
        myObj.plotScatterGraph()


    Examples:

    myObj.TwoDGraph(6, [1, 2, 3, 4, 5, 6], [2, 4, 7, 9, 10, 12], 'Graph Title', 'X-asis', 'Y-axis')
    myObj.plotLineGraph()
    myObj.plotScatterGraph()


    """

    def __init__(self, n, x, y, title='', labelX='', labelY=''):
        self.n = n
        self.x = x
        self.y = y
        self.title = title
        self.labelX = labelX
        self.labelY = labelY

    def plotScatterGraph(self):
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        ax.scatter(self.x, self.y, color='b')
        ax.set_xlabel(self.labelX)
        ax.set_ylabel(self.labelY)
        ax.set_title(self.title)
        pyplot.show()

    def plotLineGraph(self):
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel(self.labelX)
        ax.set_ylabel(self.labelY)
        ax.set_title(self.title)
        pyplot.plot(self.x, self.y)

        # for showing the coordinates of the points
        for i, j in zip(self.x, self.y):
            ax.annotate(str(f'({i}, {j}'), xy=(i, j))

        pyplot.show()

    @classmethod
    def getUserInput(cls):
        while True:
            try:
                title = input('Enter title of the scatter graph: ')
                labelX = input('Enter label for X-axis: ')
                labelY = input('Enter label for Y-axis: ')
                n = int(input('Enter number of coordinates you will enter: '))
                print('Enter x coordinates separated by spaces: ', end='')
                x = list(map(float, input().split(' ')))
                print('Enter y coordinates separated by spaces: ',  end='')
                y = list(map(float, input().split(' ')))
                assert(len(x) == n and len(y) == n)
                return cls(n, x, y, title, labelX, labelY)
            except:
                print('Please make sure you give valid input!!')
                continue


class ThreeDGraph:
    """
    Creating an object
        myObj = TwoDGraph(x, y, z, title, labeX, labelY, labelZ)

    Now if you want to plot 
    3-d Line Graph:
        myObj.plotLineGraph()

    3-d Scatter graph:
        myObj.plotScatterGraph()

    3-d Surface graph:
        myObj.plotSurfaceGraph()


    Example Usage:

    3-d line graph
    ---------------
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    obj = ThreeDGraph(x, y, z, '3-D line graph', 'values of x', 'values of y', '')
    obj.plotLineGraph()

    3-d surface graph
    -----------------
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    obj = ThreeDGraph(X, Y, Z, '3-D surface graph', 'values of x', 'values of y', '')
    obj.plotSurfaceGraph()


    3-d scatter graph
    -----------------
    n=100
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, -50, -25)
    obj = ThreeDGraph(xs, ys, zs, '3-D Scatter graph', 'values of x', 'values of y', '')
    obj.plotScatterGraph()
    """

    def __init__(self, x, y, z, title='', labelX='', labelY='', labelZ=''):
        self.x = x
        self.y = y
        self.z = z
        self.title = title
        self.labelX = labelX
        self.labelY = labelY
        self.labelZ = labelZ

    def plotLineGraph(self):
        fig = pyplot.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel(self.labelX)
        ax.set_ylabel(self.labelY)
        ax.set_title(self.title)
        ax.plot(self.x, self.y, self.z, label='parametric curve')
        ax.legend()
        pyplot.show()

    def plotScatterGraph(self):
        fig = pyplot.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel(self.labelX)
        ax.set_ylabel(self.labelY)
        ax.set_title(self.title)
        ax.scatter(self.x, self.y, self.z, c='r', marker='o')
        ax.legend()
        pyplot.show()

    def plotSurfaceGraph(self):
        fig = pyplot.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel(self.labelX)
        ax.set_ylabel(self.labelY)
        ax.set_title(self.title)
        ax.plot_surface(self.x, self.y, self.z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        pyplot.show()


"""
Ref:
https://matplotlib.org/
"""