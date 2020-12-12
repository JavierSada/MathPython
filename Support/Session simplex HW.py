print ("\nTransportation LP problem === optimization costs")
import numpy as np
from scipy.optimize import linprog
c= ([[8, 12, 15, 13, 10, 17], [15, 18, 16, 12, 13, 14], [10, 11, 12, 16, 18, 9], [19, 14, 17, 15, 17, 16]])
A= ([[32000, 38000, 44000, 52000, 36000, 22000]])
b= ([[56000, 48000, 62000, 54000]])
print "checking"