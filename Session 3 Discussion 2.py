import random
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    r = random.random()
    y = x-10*r-x**r
    return y

def Correlation(x, y):
    plt.scatter(x, y)
    par = np.polyfit(x, y, 1)
    plt.plot(np.unique(x), np.poly1d(par)(np.unique(x)))
    R = np.corrcoef(x,y)[1,0]
    plt.text(20,80,'$R = %0.4f$'% R, fontsize=20)
   
random.seed(150) 
x_values = np.array(range(1,120))
y_values = [f(x) for x in x_values]
n = len(x_values)

Correlation(x_values, y_values)
plt.plot(x_values, y_values)
plt.show()