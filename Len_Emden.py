import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,t, params):
	d, omega = y
	n, k = params
	derivs = [omega, -2*omega*k/t - d**n]
	return derivs

N = float(input("Enter the value of n: "))
k = 1
params = [N,k]

d0 = 1.0
omega0 = 0.0

y0 = [d0, omega0]


# Timeseries upto 12 units of time
#  
t = np.arange(0.0001, 12, 0.01)

psoln = odeint(f, y0, t, args=(params,))



plt.plot(t, psoln[:,0])
plt.title('Dn(zeta) vs zeta')
plt.xlabel('zeta')
plt.ylabel('Dn(zeta)')
plt.show()
