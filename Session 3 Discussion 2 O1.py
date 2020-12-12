import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
 r = random.random() # A function to generate example y values
 y = x-10*r-x**r # y = x-10r-x**r
 return y

def plot_BestFitLine(x,y):
 plt.scatter(x, y) 
 par = np.polyfit(x, y, 1)
 plt.plot(np.unique(x), np.poly1d(par)(np.unique(x)))
 R = np.corrcoef(x,y)[1,0]
 plt.text(20,80,'$R = %0.4f$'% R, fontsize=20)

random.seed(113) # Ensures that we all generate the same random numbers
x_values = range(1,101)
y_values = [f(x) for x in x_values]

plot_BestFitLine(x_values, y_values)
plt.show()