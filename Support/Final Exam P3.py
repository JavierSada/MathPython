from numpy import *
from matplotlib.pyplot import *

x_28 = linspace(0, 28, 200)

y_28 = (0.00804*(x_28**3)) + (0.6519*(x_28**2)) + (2.85*x_28) + 50

x_56 = linspace(28, 56, 200)

y_56 = -1097 + 68.9*x_56


figure()
plot(x_28, y_28)
plot(x_56, y_56)

title("Problem 3")
show()

grid(True)
savefig("plot.png")