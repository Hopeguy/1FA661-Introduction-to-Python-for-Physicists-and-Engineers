

#Assignment 2

#ma = F, intergerata 2 gånger för att få fram positionen

import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Question 1

prot_joule = 1*(10**6)*sp.constants.eV  #proton energy in joule
prot_mass = sp.constants.m_p #mass of proton
prot_vel = np.sqrt(2*prot_joule/prot_mass) # from 
prot_charge = sp.constants.e
mag_field = np.array([0,0,3]) #T, array to represent the magnetic field with B value

time = np.linspace(0,10**-6,500) # looking over 500 points of a microsecond
start = np.array([0,0,0,prot_vel,0,0]) # start point for the proton, "starting in origo"

def plt_2d(figure,x,y,x_label,y_label,titel):
    plt.figure(figure)
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(titel)

def fun(y,t):
    dx = y[3]
    dy = y[4]
    dz = y[5]
    return np.concatenate(([dx,dy,dz],(prot_charge*np.cross(y[3:],mag_field))/prot_mass)) 
#return an array with the same structures as "start", but with calculated changes of the protions velocity in x,y,z depening on the magnetic field  

solution = odeint(fun,start,time)

plt_2d(1, solution[:,0], solution[:,1], 'x-axis [m]', 'y-axis [m]', '#Q1: Proton with 1 MeV in 3T Magnetic field, x and y')

#Question 2
mag_field = np.array([0,0,1]) #New magnetic field compared to first question
x_vel = prot_vel*np.sin(np.pi/4)    #divide the velocity into two; a z and x direction
z_vel = prot_vel*np.cos(np.pi/4)    

time2 = np.linspace(0,10**-6,500) # looking over 500 points of a microsecond
start2 = np.array([0,0,0,x_vel,0,z_vel])

solution2 = odeint(fun,start2,time2)

plt_2d(2, solution2[:,0], solution2[:,2], 'x-axis [m]', 'z-axis [m]', '#Q2: Proton with 1 MeV in 1 Magnetic field, x and z')

plt_2d(3, solution2[:,0], solution2[:,1], 'x-axis [m]', 'y-axis [m]', '#Q2: Proton with 1 MeV in 1 Magnetic field, x and y')

#plt_2d(4, solution2[:,0], solution2[:,2], 'x-axis [m]', 'z-axis [m]', '#Q2: Proton with 1 MeV in 1 Magnetic field, x and z')


#Question 3

time3
start3 =np.array([0,0,0,0,0,prot_vel]) #array [x,y,z,vx,vy,vz] starting in origo, launch staight up in z direction (positive)

def fun_2(y,t):
    R = np.sqrt(y[0]**2 + y[1]**2) # Pyth to find the distance from z-axis(origo), using x and y values
    cos_phi = y[0]/R #using polar coordinates as we are looking at an magnetic field around z-axis
    sin_phi = y[1]/R 


#Question 4

from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure(5)
ax = fig.add_subplot(projection='3d')
Axes3D.plot(ax, solution2[:,0],solution2[:,1],solution2[:,2])
#ax.view_init(30, 35)
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.set_title('3D view over 1 MeV proton in 1T Magnetic field')







#Question 6, drag: få fram tiden för ett varv "tiden att komma tillbaka till samma x och y" är alltså
#skillnaden i z postition som är ri
