# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid
from scipy.optimize import fsolve
from math import fabs, sqrt

class Func:
    def __init__(self, point1, line1, line2):
        self.x0=point1['x']; self.y0=point1['y'];
        self.A1=line1['A']; self.B1=line1['B']; self.C1=line1['C'];
        self.A2=line2['A']; self.B2=line2['B']; self.C2=line2['C'];
    def __call__(self,x):
        k1 = -self.A1/self.B1; b1=-self.C1/self.B1;
        k2 = -self.A2/self.B2; b2=-self.C2/self.B2;
        return [x[0]*self.x0**2 + x[1]*self.x0*self.y0 + x[2]*self.y0**2 - 1,
                (x[1]*b1 + 2*x[2]*k1*b1)**2-4*(x[0] + x[1]*k1 + x[2]*k1**2)*(x[2]*b1**2 - 1),
                (x[1]*b2 + 2*x[2]*k2*b2)**2-4*(x[0] + x[1]*k2 + x[2]*k2**2)*(x[2]*b2**2 - 1)]

def calculateEllipseParams(point1, line1, line2):
    ellipse = dict()
    func = Func(point1, line1, line2)
    root = fsolve(func, [1, 1,2]) #подправить коэффициенты начального приближения
    print(root)
    ellipse['A'] =  root[0]; ellipse['B'] = root[1]; ellipse['C'] = root[2];
    ellipse['D'] =0; ellipse['E'] = 0; ellipse['F'] = -1
    return ellipse

def plotResults( line1, point1, line2,  ellipse ) :
    delta = 0.025
    xrange = arange(-10., 10., delta)
    yrange = arange(-10., 10., delta)
    X, Y = meshgrid(xrange,yrange)
    
    A0 = ellipse['A']; B0 = ellipse['B']; C0 = ellipse['C']; 
    D0 = ellipse['D']; E0 = ellipse['E']; F0 = ellipse['F'];
       
    A1 = line1['A']; B1 = line1['B']; C1 = line1['C']
    A2 = line2['A']; B2 = line2['B']; C2 = line2['C']
        
    Ellipse = A0*(X**2) + B0*(X*Y) + C0*(Y**2) + D0*X + E0*Y + F0
    Line1   = A1*X + B1*Y + C1
    Line2   = A2*X + B2*Y + C2
    
    matplotlib.pyplot.contour(X, Y, Ellipse, [0])
    matplotlib.pyplot.contour(X, Y, Line1  , [0])
    matplotlib.pyplot.contour(X, Y, Line2  , [0])
    
    matplotlib.pyplot.plot   (point1['x'], point1['y'], 'bo' )

    matplotlib.pyplot.grid()    
    matplotlib.pyplot.show()
        
    delta = 0.025
    xrange = arange(-5.0, 5.0, delta)
    yrange = arange(-5.0, 5.0, delta)
    X, Y = meshgrid(xrange,yrange)


def conditionExistence(ellipse):
    A = ellipse['A']
    B = ellipse['B']
    C = ellipse['C']
    return B**2-4*A*C<0
#print(conditionExistence(ellipse))


def getLineParameters(line1):
    x1 = line1['x1']
    y1 = line1['y1']

    x2 = line1['x2']
    y2 = line1['y2']

    params = {'A': (y1 - y2), 'B': (x2 - x1), 'C': (x1 * y2 - x2 * y1)}

    return params

def distBetweenPnL( p, line):

    return fabs(line['A'] * p['x'] + line['B'] * p['y'] + line['C'])/sqrt(line['A']**2+line['B']**2)

def tangentPoint(p,line):
    A = line['A']; B = line['B'] ; C = line['C']
    x0 = p['x']; y0 = p['y']

    x = (B*(B*x0 - A * y0) - A*C)/(A**2 + B**2)
    y = (A*(-B*x0 + A * y0) - B*C)/(A**2 + B**2)

    point = {'x': x, 'y': y}
    return point

def realEllipse(ellipse, center):
    A = ellipse['A'];    B = ellipse['B'];    C = ellipse['C'];
    D = ellipse['D'];    E = ellipse['E'];    F = ellipse['F'];


        
if __name__ == '__main__':

    line2 = dict()
    line2['A'] = -2; line2['B'] = 1; line2['C'] = -4
    
    line1 = dict()
    line1['A'] = 2; line1['B'] =1; line1['C'] = -6
    point1 = {'x':-2, 'y':0}  #точка касания
    
    center = dict()
    ellipse = calculateEllipseParams(point1, line1, line2)
    
    plotResults(line1, point1, line2, ellipse)

    print(getLineParameters({'x1': 0, 'y1': 0, 'x2': 1, 'y2': 1}))
    point = {'x': 0, 'y': 0}

    print(distBetweenPnL(point, line1))
    print(tangentPoint(point, line1))