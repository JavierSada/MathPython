import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

z = sy.symbols('z')
sy.init_printing(use_unicode=True)
a = 0
b = 4

function = 2*z
print 'f(x) = ', function

I = sy.integrate(function)
print 'F(x) = ', I

Area = sy.integrate(function, (z, a, b))
print 'Total Area = ', Area, ' = ', "%6.3f" % Area

c = np.sqrt(float(Area)/(b-a))
print c
fc = float(function.subs(z,c).evalf(2))

pointsnum = 200
x = np.linspace(a, b, pointsnum)
f = np.zeros(pointsnum, float)
g = np.zeros(pointsnum, float)

for i in range(0, pointsnum):
    f[i] = x[i] ** 2
    g[i] = fc

plt.plot(x, f, 'k-' , lw=2)
plt.fill_between(x, f, 0, alpha=1, color= '#F5591E')
plt.plot(x, g, 'k-' , lw=1.5)
plt.fill_between(x, g, 0, alpha=0.6, color= '#5A7FAE')
plt.plot(c, 0, 'yo')
plt.plot(c, fc, 'yo')
plt.axhline(color='black', lw =1)
plt.axvline(color='black', lw =1)
plt.ylim(0, b ** 2)

plt.title ('Definite Integral of '+ str(function) + "      Area = " +str(Area))
plt.show()