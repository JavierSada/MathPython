print ("\nProblem 4 Mid Term")
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *
import matplotlib.pyplot as plt
figure()
x= arange(0,50.1,0.1)
y= arange(0,50.1,0.1)
y1 = 35-1*x 
y2 = 20-1*x
y3 = y*0+10
plot(x, y1, 'crimson')
plot(x, y2, 'navy')
plot(x, y3, 'gold')
xlim(0,50)
ylim(0,50)
xy = [0,40,0,40]
plt.axis(xy)
xy_axes = plt.plot([-11,11],[0,0],[0,0],[-11,11])
legend(['s+ a <= 35', 's + a => 20', 'a => 10'])
grid(True)
title ('Graphic Solution Problem 5 Mid Term')
xlabel('X')
ylabel('Y')
plt.show()

print('\nCorners of feasible region')
x=[0.0, 0.0, 10.0, 25.0]
y= [20.0, 35.0, 10.0, 10.0] 
P1 = 2400*0+1100*20
P2 = 2400*0+1100*35
P3 = 2400*10+1100*10
P4 = 2400*25+1100*10
print ('\nX values = %r')% x
print ('\nY values = %r')% y
print ('\nEvaluate X & Y matrix based on the corner points given R= 2400s + 1100a')
print('\nPoint 1 x=0 y=20 is equal = %r')% P1
print('\nPoint 2 x=0 y=35 is equal = %r')% P2
print('\nPoint 3 x=10 y=10 is equal = %r')% P3
print('\nPoint 4 x=25 y=10 is equal = %r')% P4
print('\nPrint the minimum point is at P2, X=0, Y=20'), 'and the amount is','$', P1