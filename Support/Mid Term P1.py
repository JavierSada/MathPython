print ('\nPython Coding Problem 1 Mid Term')
import matplotlib.pyplot
import pylab
from matplotlib.pyplot import *
import numpy as np
from numpy import linspace

x_values = (9, 2, 3, 4, 2, 5, 9, 10)
y_values = (85, 52, 55, 68, 67, 86, 83, 73)

n = len(x_values)
x= sum(x_values)
y= sum(y_values)
xy = np.dot(x_values, y_values)
x2 = np.dot(x_values, x_values)
y2 = np.dot(y_values, y_values)

m = (n*xy-x*y)/(n*x2-x**2)
b = (y-m*x)/n

figure()
matplotlib.pyplot.scatter(x_values,y_values)
grid(True)
x = linspace(0,10,10)
y = round(m,10)*x + round(b,10)
plot(x,y,'b')
title('Least Squares Line\ny = 2.7885 * x + 55.788')
show()