# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:13:08 2021

@author: jocke
"""

#perp work with ODEINT

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t):
    k = 0.3
    dydt = -k*y
    return dydt

#initial condition
y0 = 5
#time points
t = np.linspace(0,20) #standard is 50 points inbetween start and stop value

#solve ode
y = odeint(model, y0, t)

# plot results
plt.figure(1)
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#Same thing with but now we have different constant "k" that can be inputed

def model(y,t,k):
    dydt = -k*y
    return dydt

#initial condition
y0 = 5
#time points
t = np.linspace(0,20) #standard is 50 points inbetween start and stop value

#solve ode
k = 0.1
y1 = odeint(model, y0, t, args=(k,))
k = 0.2
y2 = odeint(model, y0, t,args=(k,))
k = 0.5
y3 = odeint(model,y0,t, args=(k,))

# plot results
plt.figure(2)
plt.plot(t, y1, 'r-', linewidth = 2, label = 'k=0.1')
plt.plot(t, y2, 'b--', linewidth = 2, label = 'k=0.2')
plt.plot(t, y3, 'g:', linewidth = 2, label = 'k=0.5')
plt.legend(loc = 'best')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#Problem 1

def model2(y,t):
    dydt = -y + 1
    return dydt

# initial condition
y0 = 0

#time points
t = np.linspace(0,5)

#solve ode
y = odeint(model2, y0, t)

# plot results
plt.figure(3)
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#problem 2
def model3(y,t):
    if t<10:
        u = 0.0
    else:
        u = 2.0
    dydt = (-y + u)/5.0
    return dydt

# initial condition
y0 = 1

#time points
t = np.linspace(0,35)

#solve ode
y = odeint(model3, y0, t)

# plot results
plt.figure(4)
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#problem 3
def model4(z,t): #function used in the ODEINT solver, aka the function for the dx/dt, or dy/dt. this one solves both at the same time.
    x = z[0]
    y = z[1]
    dxdt = 3 * np.exp(-t)
    dydt = 3 - y
    return [dxdt, dydt]


# initial condition
z0 = [0,0]

#time points
t = np.linspace(0,10)

#solve ode
z = odeint(model4, z0, t)
x = z[:,0]
y = z[:,1]


#plot results
plt.figure(5)
plt.plot(t, x, 'r-')
plt.plot(t, y, 'b--')
plt.xlabel('time')
plt.legend(['x(t)','y(t)'])
plt.show()


#problem 4

def model5(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x+u)/2.0
    dydt = (-y+x)/5.0
    return [dxdt, dydt]

# initial condition
z0 = [0,0]

#time points
n = 150
t = np.linspace(0,15,n)
u = np.zeros(n)     #creats an list filled with zeros
u[51:] = 2.0    #changes the list so that after time = 5, u is now 2 instead of 0, "step function"

x = np.zeros(n)  #Creats the list beforehands to be filled in in the for loop
y = np.zeros(n)
  
#solve ode
for i in range(1, n):   #for loop the goes trhough all the values except the starting value as that was given before
    # tspan = [t[i-1], t[i]]
    z = odeint(model5, z0, t, args=(u[i],)) # solves the ODE, with the extra argument with u changing depnding on what time step we are on
    z0 = z[1]   #gets the new value for the initial condition before using it in the ODE again
    x[i] = z0[0]    #inputs the x and y values that were solved for in the ODE
    y[i] = z0[1]


# plot results
plt.figure(6)
plt.plot(t,u,'k:') #Plots the step function showing that at t = 5 it changes to 2
plt.plot(t, x, 'r-')
plt.plot(t, y, 'b--')
plt.xlabel('time')
plt.legend(['u(t)','x(t)', 'y(t)'])
plt.show()