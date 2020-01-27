import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D


class Pol:
    def __init__(self, n, s, b):
        self.n = n
        self.t = np.arange(-b, b, 0.01)
        self.s = s
        plnm = 0
        for i in range(n+1):
            plnm += self.s[i]*self.t**i
        self.plnm = plnm


class var2pol:
    def __init__(self, n1, n2, c, s1, s2, s12, b1, b2):
        self.n1 = n1
        self.n2 = n2
        self.c = c
        self.s1 = s1
        self.s2 = s2
        self.s12 = s12
        self.b1 = b1
        self.b2 = b2

        self.u = np.arange(-b1, b1, 0.01)
        self.v = np.arange(-b2, b2, 0.01)

        self.u, self.v = np.meshgrid(self.u, self.v)

        plnm = 0
        for i in range(n1):
            plnm += self.s1[i] * self.u ** i
        plnm1 = plnm

        plnm = 0
        for i in range(n2):
            plnm += self.s2[i] * self.v ** i
        plnm2 = plnm

        plnm = 0
        for i in range(n1):
            for j in range(n2):
                plnm += self.s12[i][j] * self.u ** i * self.v ** j
        plnm12 = plnm

        self.plnm = self.c + plnm1 + plnm2 + plnm12


def plotc(x, y, z, num):
    fig1 = pylab.figure(1)
    axes1 = Axes3D(fig1)

    fig1 = axes1.plot3D(x, y, z)

    pylab.savefig('test_images/c/test{}'.format(num) + '.png')

    pylab.show(fig1)

def plots(x, y, z, num):
    fig = pylab.figure(1)
    axes = Axes3D(fig)

    fig = axes.plot_surface(x, y, z)
    pylab.savefig('test_images/s/test{}'.format(num) + '.png')

    pylab.show(fig)

def curve(num):
    x = []
    nam = ["x", "y", "z"]
    for j in range(3):
        print(nam[j], ":")
        n = int(input("n= "))
        s = []
        for i in range(n+1):
            tv = float(input("kt^{}:    k=".format(i)))
            s.append(tv)
        b = float(input("b ="))
        x.append(Pol(n, s, b))
    var = []
    for xi in x:
        var.append(xi.plnm)
    plotc(var[0], var[1], var[2], num)
    plt.plot(var[0], var[1])
    plt.plot(var[1], var[2])
    plt.plot(var[2], var[0])
    plt.show()

def surface(num):
    x = []
    nam = ["x", "y", "z"]
    b1 = float(input("b1= "))
    b2 = float(input("b2= "))
    for j in range(3):
        print(nam[j], ":")
        n1 = int(input("n1= "))
        n2 = int(input("n2= "))
        c = float(input("c= "))
        s1 = []
        for i in range(n1):
            tv = float(input("ku^{}:    k=".format(i+1)))
            s1.append(tv)
        s2 = []
        for i in range(n2):
            tv = float(input("kv^{}:    k=".format(i+1)))
            s2.append(tv)
        s12 = []
        for i1 in range(n1):
            ts = []
            for i2 in range(n2):
                tv = float(input("ku^{}v^{}:    k=".format(i1+1, i2+1)))
                ts.append(tv)
            s12.append(ts)
        x.append(var2pol(n1, n2, c, s1, s2, s12, b1, b2))
    var = []
    for xi in x:
        var.append(xi.plnm)
    plots(var[0], var[1], var[2], num)
    plots(x[0].u, x[0].v, var[0], num+1)
    plots(x[0].u, x[0].v, var[1], num+2)
    plots(x[0].u, x[0].v, var[2], num+3)

counters = 0
counterc = 0
while True:
    try:
        ch = int(input("curve - 1 \n surf - 2 \n exit - 0 \n  "))

        if ch == 1:
            counterc += 1
            curve(counterc)
        elif ch == 2:
            counters += 4
            surface(counters/4)
        elif ch == 0:
            break
        else:
            print("err")
    except ValueError:
        print("err")


