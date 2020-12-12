print ("\nProblem 1 Final Exam")
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *
import matplotlib.pyplot as plt
figure()
x= arange(0,50.1,0.1)
y= arange(0,50.1,0.1)
y1 = 3-1*x
y2 = 10-1*x
y3 = -3+1*x
of = 7.833-0.66*x
plot(x, y1, 'blue')
plot(x, y2, 'r')
plot(x, y3, 'g')
plot(x, of, 'k--')
title ('Graphic Solution Problem 1 Final Exam')
legend(['Constrain 1 is x+y => 3', 'Constrain 2 is x+y <= 10', 'Constrain 3 is x-y => 3', 'Objective Function y = 7.833 - 0.66x'])
xlabel('X - axis')
ylabel('Y - axis')
plt.fill([3,6.5,10],[0,3.5,0],'grey',alpha=0.5)
xlim(0,15)
ylim(0,15)
grid(True)
plt.show()
print('\nCorners of feasible region')
x=[3.0, 6.5, 10.0]
y= [0.0, 3.5, 0.0] 
print ('\nX values = %r')% x
print ('\nY values = %r')% y
P1= 4*3.0+6*0
P2= 4*6.5+6*3.5
P3= 4*10.0+6*0
print ('\nEvaluate points in feasabel region according to z= 4x+6y=47')
print('\nPoint 1 x= 3 y= 0 is equal = %r')% P1
print('\nPoint 1 x= 6.5 y= 3.5 is equal = %r')% P2
print('\nPoint 1 x= 10 y= 0 is equal = %r')% P3
alist=[P1, P2, P3]
largest=alist[0]
for large in alist:
    if large > largest:
        largest=large
print(largest)
print('\nPrint the maximum point is at P2, X=6.5, Y=3.5'), 'and the amount is', P2
