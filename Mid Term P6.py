print ("\nProblem 6 Mid Term")
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *

figure()
x= arange(0,60.1,0.1)
y= arange(0,60.1,0.1)
y1= 20-0.2*x
y2= 27.5-0.5*x
y3= 33.3-0.66*x
xlim(0,60)
ylim(0,40)
plot(x, y1, 'darkred')
plot(x, y2, 'darkblue')
plot(x, y3, 'gold')
xlabel('X')
ylabel('Y')
grid(True)
title ('Solution Problem 6 Mid Term')
legend(['x + 5y <= 100', 'x + 2y <= 55 ', '2x + 3y = 100'])
show()