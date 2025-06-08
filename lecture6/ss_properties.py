import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import scipy as sp

s = tf([1,0], [1])  # laplace variable

g = 6205 / (s * (s**2 + 13*s + 1281))
heq = (g / (1+g)).minreal()

for pole in poles(heq):
    if pole.imag == 0:        
        tau = -1/pole.real  # getting tau from the real pole
    else:
        a = pole.real  # getting the a + bi stuff to find w_n and zeta
        b = pole.imag

# h1 is first order 
h1 = (1/tau) / ((1/tau) + s)

# h2 is second order
w_n = np.sqrt(a**2 + b**2)  # frequency from the complex conjugate a + bi
zeta = -a / w_n  # damping ratio 

h2 = w_n**2 / (w_n**2 + 2*zeta*w_n*s + s**2)
print((h1*h2).minreal(), heq)  # yayy! they are the same

t = np.arange(0, 2.01, 0.01)

y1 = step(h1, t)
y2 = step(h2, t)
yeq = step(heq, t)

plt.plot(t, y1[0], color='blue')
plt.plot(t, y2[0], color='red')
plt.plot(t, yeq[0], color='green')
plt.show()

dif1 = np.absolute(yeq[0] - y1[0])
dif2 = np.absolute(yeq[0] - y2[0])

D1 = sp.integrate.trapezoid(dif1, t)
D2 = sp.integrate.trapezoid(dif2, t)

print("D1", D1)
print("D2", D2)