
#LAB 4
from scipy.integrate import odeint
import scipy


#Question 1
g = scipy.constants.g

def projectile(t,y):
    
    dydt = [y_arr[3],y_arr[4],y_arr[5],0,0,g]
    return dydt 

x, y, z = 0, 0, 0
vx, vy, vz = 1, 0, 20
y_arr = [x,y,z,vx,vy,vz]    
times = range(0,50)

solution = odeint(projectile, y_arr, times)

plot

