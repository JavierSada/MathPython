# -*- coding: utf-8 -*-
print ('\nSolving Module 1 problem Session 2')
import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy 
from numpy import linspace
figure()
x=linspace(0,100,100)
y=0.056057*x*x+1.06657*x
y55=0.056057*(55)**2+1.06657*(55)
xlabel('MPH')
ylabel('Distance')
title ('Plot of Stopping Distance versus Speed')
scatter(55,y55,c='y',s=40)
plot(x,y)
show()

print ('\nSolving Module 2 problem Session 2')
C=array([[22,25,38],[31,34,35]])
print ('\nArray C')
print C
K=array([[5,10,8],[11,14,15]])
print ('\nArray K')
print K
M=C-K
print ('\nResult of Subtraction')
print M
print ('\nSecond Row of Result is %s') %M[1,:]
print ('Third Column of Result is %s') %M[:,2]
print (‘Common Element is %r’) %M[1,2]
Array C
[[22 25 38]
[31 34 35]]
Array K
[[ 5 10 8]
[11 14 15]]
Result of Subtraction
[[17 15 30]
[20 20 20]]
Second Row of Result is [20 20 20]
Third Column of Result is [30 20]
Common Element is 20