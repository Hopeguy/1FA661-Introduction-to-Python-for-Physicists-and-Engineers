#--------------------Assignment 2------------------

import numpy as np
import scipy.constants as const
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#---------------Functions---------------

def plt_2d(figure,x,y,x_label,y_label,titel): #functions to make and save all 2d plots
    plt.figure(figure)
    plt.plot(x,y)
    plt.xlabel(x_label)     
    plt.ylabel(y_label)
    plt.title(titel)
    plt.savefig(titel)

def get_pos(y,t): #function used for question 1 and 2
    return np.concatenate(([y[3],y[4],y[5]],(prot_charge*np.cross(y[3:],mag_field))/prot_mass)) 
#return an array with the same structures as "start", but with calculated changes of the protions velocity in x,y,z depening on the magnetic field  


#------------------Question 1--------------------

prot_joule = 1*(10**6)*const.eV  #proton energy in joule 
prot_mass = const.m_p #mass of proton
prot_vel = np.sqrt(2*prot_joule/prot_mass) # from 
prot_charge = const.e
mag_field = np.array([0,0,3]) #T, array to represent the magnetic field with B value

time = np.linspace(0,10**-6,1000) # looking over 1000 points of a microsecond
start = np.array([0,0,0,prot_vel,0,0]) # start point for the proton, "starting in origo"


solution = odeint(get_pos,start,time)

plt_2d(1, solution[:,0], solution[:,1], 'x-axis [m]', 'y-axis [m]', 'Q1 Proton with 1 MeV in 3T Magnetic field, x and y')
plt_2d(2, solution[:,0], solution[:,2], 'x-axis [m]', 'z-axis[m]', 'Q1 Proton with 1 MeV in 3T Magnetic field, x and z')


#--------------------Question 2-----------------

mag_field = np.array([0,0,1]) #New magnetic field compared to first question
x_vel = prot_vel*np.sin(np.pi/4)    #divide the velocity into two; a z and x direction
z_vel = prot_vel*np.cos(np.pi/4)    

start2 = np.array([0,0,0,x_vel,0,z_vel])

solution2 = odeint(get_pos,start2,time)

plt_2d(3, solution2[:,0], solution2[:,2], 'x-axis [m]', 'z-axis [m]', 'Q2 Proton with 1 MeV in 1 Magnetic field, x and z')

plt_2d(4, solution2[:,0], solution2[:,1], 'x-axis [m]', 'y-axis [m]', 'Q2 Proton with 1 MeV in 1 Magnetic field, x and y')


#-------------------Question 3------------------

start3 =np.array([3,3,0,0,0,prot_vel]) #array [x,y,z,vx,vy,vz] starting 3 meters out from origo, on the x-axis, launch staight up in z direction (positive)

def get_pos_2(y,t):   #function used for solving question 3
    R = y[0] # Due to being cylindrical around the z axis, the radius = magnitude of position vector
    cos_phi = y[0]/R #using polar coordinates as we are looking at an magnetic field going around the z-axis
    sin_phi = y[1]/R 
    B_x = sin_phi*9/R # magnetic field strength in x direction
    B_y = -cos_phi*9/R # magnetic field strength in y direction
    
    mag_field = np.array([B_x,B_y, 0]) #new magnetic field depending on the components in x and y (around z-axis)
    
    return np.concatenate(([y[3],y[4],y[5]],(prot_charge*np.cross(y[3:],mag_field))/prot_mass)) 


solution3 = odeint(get_pos_2, start3, time) #solves the diff equation for question 3, using the function the taking into account the new circular magnetic field

plt_2d(5, solution3[:,0], solution3[:,2], 'x-axis [m]', 'z-axis [m]', 'Q3 Proton with 1 MeV in 1 Magnetic field, going around z-axis')
plt_2d(6, solution3[:,0], solution3[:,1], 'x-axis [m]', 'y-axis [m]', 'Q3 Proton with 1 MeV in 1 Magnetic field, x and y axis')


#-----------------Question 4---------------------

#Plots the 3D plot of question 2

fig =plt.figure(7)
ax = fig.add_subplot(projection='3d')
Axes3D.plot(ax, solution2[:,0],solution2[:,1],solution2[:,2])
ax.view_init(30, 35)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.set_title('3D view over 1 MeV proton in 1T Magnetic field')
fig.savefig('Q4 3D plot of question 2')


#---------------Question 5----------------------

#Plots the 3D plot of question 3
fig =plt.figure(8)
ax = fig.add_subplot(projection='3d')
Axes3D.plot(ax, solution3[:,0],solution3[:,1],solution3[:,2])
ax.view_init(20, 10)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.set_title('3D view over 1 MeV proton in 1T Magnetic field going around z-axis')
fig.savefig('Q5 3D plot of question 3')


#-----------------Question 6-----------------------

plt_2d(9, time, solution3[:,2], "time", "z-axis", "Q6 difference in z-axis depending on time")
"""
at index 157 in the solution3 we have one full rotation
where we have the same x and y values again
but z have changed due to drift speed

this was found by manually going through the variable explorer for the next
time both x and y had the same values as the start values [3,3]

"""
drift = (solution3[0,2] - solution3[157,2])/time[157] #calculates the drift speed in meter/s
print(drift) #Prints the drift speed in m/s