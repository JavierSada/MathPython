import random
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    # A function to generate example y values
    r = random.random()
    y = x-10*r-x**r
    return y
random.seed(352) # Ensures that we all generate the same random numbers
x_values = np.array(range(1,101)) # Numbers from 1 to 100
y_values = np.array([f(x) for x in x_values]) # Get y value for each x value
n = len(x_values) # the number of observationsT
sumx= np.sum(x_values)
sumy= np.sum(y_values)
sumx_y=np.sum(x_values*y_values)
squarex= np.sum(x_values**2)
squarey= np.sum(y_values**2)
slope= round((n *(sumx_y)) - (sumx * sumy))/((n * sumx) - sumx**2)
print "The slope is equal to:", slope 
b = round(sumy - (slope * sumx))/n
print "The intercept is equal to:", b
plt.plot(x_values, y_values)
print "The best equation is:", "+",("y=%s"%slope+"x +%s"%b)
