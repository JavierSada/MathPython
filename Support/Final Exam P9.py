from numpy import *
from matplotlib.pyplot import *
from math import *

import numpy as np
import matplotlib.pyplot as plt

def ddash(x):
    return 4/x + 5
def d(x):
    return 4 * np.log((x + 5)/6) + 2.5

plt.figure(figsize=(12,6))

plt.subplot(211)
x_axis = np.linspace(-2, 2,num = 500)
y_axis = d(x_axis)
plt.plot(x_axis,y_axis, 'g--')
plt.title('D(x) = 4 * In [(x + 5)/6] +2.5')
grid(True)
plt.subplot(212)
x_axis = np.linspace(-2, 2,num = 500)
y_axis = ddash(x_axis)
plt.plot(x_axis,y_axis, 'r')
plt.title("D'(x) = 4 / x + 5")
grid(True)
plt.show()