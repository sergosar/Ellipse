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
    #dict, dict, dict
    def __init__(self, point1, line1, line2):
        self.x0 = point1['x']; self.y0 = point1['y'];
        self.A1 = line1['A']; self.B1 = line1['B']; self.C1 = line1['C'];
        self.A2 = line2['A']; self.B2 = line2['B']; self.C2 = line2['C'];
    def __call__(self,x):
        k1 = -self.A1/self.B1; b1 = -self.C1/self.B1;
        k2 = -self.A2/self.B2; b2 = -self.C2/self.B2;
        return [x[0]*self.x0**2 + x[1]*self.x0*self.y0 + x[2]*self.y0**2 - 1,
                (x[1]*b1 + 2*x[2]*k1*b1)**2-4*(x[0] + x[1]*k1 + x[2]*k1**2)*(x[2]*b1**2 - 1),
                (x[1]*b2 + 2*x[2]*k2*b2)**2-4*(x[0] + x[1]*k2 + x[2]*k2**2)*(x[2]*b2**2 - 1)]

def calculateEllipseParams(point1, line1, line2, koeff):
    #dict,dict,dict, list
    ellipse = dict()
    func = Func(point1, line1, line2)
    root = fsolve(func, [koeff[0], koeff[1], koeff[2]]) #подправить коэффициенты начального приближения
   # print(root)
    ellipse['A'] = root[0]; ellipse['B'] = root[1]; ellipse['C'] = root[2];
    ellipse['D'] = 0; ellipse['E'] = 0; ellipse['F'] = -1
    return ellipse

def plotResults(line1, point1, line2, ellipse) :
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
    
    matplotlib.pyplot.plot(point1['x'], point1['y'], 'bo' )

    matplotlib.pyplot.grid()    
    matplotlib.pyplot.show()
        
    delta = 0.025
    xrange = arange(-5.0, 5.0, delta)
    yrange = arange(-5.0, 5.0, delta)
    X, Y = meshgrid(xrange,yrange)


def conditionExistence(ellipse):
    #dict
    A = ellipse['A']
    B = ellipse['B']
    C = ellipse['C']
    return B**2-4*A*C<0
#print(conditionExistence(ellipse))


def getLineParameters(line1):
    #input point list, output dict
    x1 = line1[0].x()
    y1 = line1[0].y()

    x2 = line1[1].x()
    y2 = line1[1].y()

    params = {'A': (y1 - y2), 'B': (x2 - x1), 'C': (x1 * y2 - x2 * y1)}

    return params

def distBetweenPnL( p, line):
    #dict, dict

    return fabs(line['A'] * p['x'] + line['B'] * p['y'] + line['C'])/sqrt(line['A']**2+line['B']**2)

def tangentPoint(p,line):
    #dict, dict, return dict
    A = line['A']; B = line['B']; C = line['C']
    x0 = p['x']; y0 = p['y']

    x = (B*(B*x0 - A * y0) - A*C)/(A**2 + B**2)
    y = (A*(-B*x0 + A * y0) - B*C)/(A**2 + B**2)

    point = {'x': x, 'y': y}
    return point


def realEllipse(point, line1, line2, center):
    #dict, list of Qpoint , Qpoint
    #rewrite
    line1Dict = getLineParameters(line1)
    line2Dict = getLineParameters(line2)

    line1Dict['C'] = line1Dict['C'] + line1Dict['A'] * center.x() + line1Dict['B'] * center.y()
    line2Dict['C'] = line2Dict['C'] + line2Dict['A'] * center.x() + line2Dict['B'] * center.y()

    point={'x': point['x']-center.x(), 'y': point['y']-center.y()}
#заглушка
    centerD = {'x': 0, 'y': 0}
    l = min([distBetweenPnL(centerD, line1Dict), distBetweenPnL(centerD, line2Dict)])
    koeff = [sqrt(l / 2), 0, sqrt(l / 2)]
#    koeff = [0.1, 0, 0.1]
    return calculateEllipseParams(point, line1Dict, line2Dict, koeff)

if __name__ == '__main__':

    line2 = dict()
    line2['A'] = -2; line2['B'] = 1; line2['C'] = -4

    line1 = dict()
    line1['A'] = 2; line1['B'] =1; line1['C'] = -6
    point1 = {'x': -2, 'y': 0}  #точка касания

    center = {'x': 0, 'y': 0}
    l = min([distBetweenPnL(center,line1), distBetweenPnL(center,line2)])
    print(l)
    koeff = [sqrt(l/2), 0, sqrt(l/2)]
    ellipse = calculateEllipseParams(point1, line1, line2, koeff)
    print(ellipse)
    plotResults(line1, point1, line2, ellipse)
#    print(getLineParameters({'x1': 0, 'y1': 0, 'x2': 1, 'y2': 1}))
    point = {'x': -2, 'y': 0}

 #   print(distBetweenPnL(point, line1))
 #   print(tangentPoint(point, line2))
    print()