import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, r, params):
	rho, omega = y
	G, gamma, k = params
	derivs = [omega,
		 ((-4*3.14*G*rho*r**2/(gamma*k)) 
		 - (2*r*rho**(gamma-2)*omega) 
		 + ((2-gamma)* r**2 * rho**(gamma-3) 
		 * omega**2))
		 /(r**2 * rho**(gamma-2))]
	return derivs

G = 6.67 * 10**-14
gamma = float(input("Enter the value of adiabatic constant gamma:"))
k = 800000

rho0 = float(input("Enter the value of central density at the core of Star: "))
omega0 = 0.0




params = [G, gamma, k]

y0 = [rho0, omega0]

r = np.arange(0.001,  2000000000, 1000000) 

mi = rho0*4*np.pi*r[0]**3/3 																																																																																																																						
mass = [mi]

psoln = odeint(f, y0, r, args = (params,))

for i in range(1,len(r)):
	m = mi + 4 * np.pi * r[i]**2 * (r[i]-r[i-1]) * psoln[:,0][i]
	mass.append(m)
	mi = m

mass = np.array(mass)/10**30
print (len(r), len(mass))

plt.figure(1)
plt.clf()
plt.subplot(2,2,1)
plt.grid()
plt.plot(r/1000,psoln[:,0])
plt.title('Density vs Radius')
plt.xlabel('Radius (in km)')
plt.ylabel('Density (in kg/m3)' )

plt.subplot(2,2,2)
plt.grid()
plt.plot(r/1000,k * psoln[:,0]**gamma/10**10, color = 'green')
plt.title('Pressure vs Radius')
plt.xlabel('Radius (in km)')
plt.ylabel('Pressure (in 10^10 Pascals)')


plt.subplot(2,1,2)
plt.grid()
plt.plot(r/1000, mass, color = 'red')
plt.title('Mass vs Radius')
plt.xlabel('Radius (in km)')
plt.ylabel('Mass (in 10^30 kg)')
plt.show()

