
#LAB 4
from scipy.integrate import odeint
import scipy
import matplotlib.pyplot as plt
import numpy as np


#Question 1
g = scipy.constants.g

def projectile_with_drag(y,t):
    
    dydt = [y[3],y[4],y[5],-y[0]*b,-y[1]*b,-g-(y[2]*b)]
    return dydt 

def projectile(y,t):
    dydt = [y[3],y[4],y[5],0,0,-g]
    return dydt 

x, y, z = 0, 0, 0  #starting position in origo
vx, vy, vz = 1, 0, 20   #starting accelaration in m/s
start = [x,y,z,vx,vy,vz]    
times = np.arange(0,10,0.01)
b = 0.5 #drag constant

solution = odeint(projectile, start, times)

def first_neg(list):
    for count, number in enumerate(list):
        if number < 0:
            return count
    


plt.figure(1)
plt.plot(times, solution[:,0], 'r--')
plt.plot(times, solution[:,1], 'b--')
plt.plot(times[0:first_neg(solution[:,2])+1], solution[0:first_neg(solution[:,2])+1,2], 'g--')
plt.legend(['x(t)', 'y(t)', 'z(t)'])
plt.ylabel('axis')
plt.xlabel('time [s]')
plt.title('Question 4')


#Question 5

x, y, z = 0, 0, 0  #starting position in origo
vx, vy, vz = 1, 0, 20   #starting accelaration in m/s
start = [x,y,z,vx,vy,vz]    
times = np.arange(0,10,0.01)
b = 0.5 #drag constant

solution_d = odeint(projectile_with_drag, start, times)

plt.figure(2)
plt.plot(times[0:first_neg(solution_d[:,0])+1], solution_d[0:first_neg(solution_d[:,0])+1,0], 'r--')
plt.plot(times, solution_d[:,1], 'b--')
plt.plot(times[0:first_neg(solution_d[:,2])+1], solution_d[0:first_neg(solution_d[:,2])+1,2], 'g--')
plt.legend(['x(t)', 'y(t)', 'z(t)'])
plt.ylabel('axis')
plt.xlabel('time [s]')
plt.title('with drag')

plt.figure(3)
plt.plot(times, solution[:,2], 'r--')
plt.plot(times, solution_d[:,2], 'b--')
plt.plot(times, np.zeros(1000),'g')
plt.legend(['with drag','without drag','Zero line'])
plt.ylabel('z-axis')
plt.xlabel('time [s]')
plt.title('with and without drag hight in m')