print ("\nProblem 4 Mid Term")
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *

figure()
x= arange(0,400.1,0.1)
y= arange(0,400.1,0.1)
y1 = 220 - 0.66*x
y2 = 372 - 2*x
y3 = [0]*len(x)
grid(True)
xlim(0,400)
ylim(0,400)
xlabel('X')
ylabel('Y')
plot(x, y1, 'crimson')
plot(x, y2, 'navy')
legend(['0.5x  +0.75y <= 165', '0.5x + 0.25y <= 93'])
fill_between(x,y2,where=(y2<=y1),color='SpringGreen')
fill_between(x,y1,where=(y1<=y2),color='SpringGreen')
title ('Solution Problem 4 Mid Term')
show()