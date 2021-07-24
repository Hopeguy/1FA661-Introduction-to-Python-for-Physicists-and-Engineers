# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:20:46 2021

@author: jocke
"""

'''
Project solar system

Joakim Ginste

# '''

import turtle as tl
import numpy as np
import matplotlib.pyplot as plt
import time


# Attempt 1

#----------Class objects-----------

class Objects:
    def __init__(self, name, pos, color, mass, vel, radius, force, momentum):
        self.name = name
        self.pos = pos
        self.color = color
        self.mass = mass
        self.vel = vel #initial velocity
        self.radius = radius
        self.force = force
        self.momentum = momentum
        
#---------Functions--------

def G_force(planet1,planet2): # calculats the garvitaional force exerted on p1 by p2 by their distances from eachother. sun is at 0

    G = 6.67*10**-20 # Gravitional constant
    
    r_vec = np.subtract(planet1.pos, planet2.pos)# calculates the distance vector between p1 and p2
    
    r_mag = np.linalg.norm(r_vec) # gives magnitude of the distance vector
    
    r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
    force_mag = G*planet1.mass * planet2.mass / (r_mag**2) # gives force magnitude

    force_vec = -force_mag*r_hat # gives force vector 
    
    return force_vec.tolist() #Output force 1 by 2



# Data and for loop for planets

#take form https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 


planets_name = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planets_pos = [[69.8,0], [108.9,0], [152.1,0], [249.2,0], [816.6,0], [1514.5,0], [3003.6,0], [4545.7,0], [7375.9,0]]  # * 10**6 km, same y value as they are starting on a line using the apehlion distance
planets_color = ['grey', 'orange', 'green', 'yellow', 'yellow', 'yellow', 'cyan', 'blue', 'grey']
planets_mass = [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102, 0.0146] #mass in kg /(10**24)
planets_vel = [[0, 47.4], [0, 35.0], [0, 29.8], [0, 24.1], [0, 13.1], [0, 9.7], [0, 6.8],[0, 5.4], [0, 4.7]] #km/s orbital velocity for each planet orbitng the sun
# planets_radius = [4879,	12104,	12756,	6792,	142984,	120536,	51,118,	49528, 2370] #diameter in km
planets_radius = [20,	20,	20,	20,	100,	100,	100,	100,   100] #own values as they are very hard to see with the acctual radius as they differ so much between the planets, they are still assumed to be point like in calculations
planets_force = [0, 0, 0, 0, 0, 0, 0, 0, 0]
planets_momentum = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

#takes the indata and makes it to SI units

# for t, planet_8 in enumerate(planets_pos):
#     planets_pos[t] = planet_8*(10**9)

for k, planet_1 in enumerate(planets_mass):
    planets_mass[k] = planet_1*(10**15)  #set standard value for all to 10**9 m

for m, planet_2 in enumerate(planets_radius):
    planets_radius[m] = planet_2/2
    
for L, planet_5 in enumerate(planets_vel):
    planets_vel[L] = [planet_5[0], planet_5[1]/(10**)]

for T, planets_6 in enumerate(planets_mass):        #gives the momenutm = velocity*mass of each planets, assumed that the velocity is in the y direction only at the start at apehlion distance from sun.
    planets_momentum[T][1] = planets_vel[T][1]*planets_6
    
Sun = Objects('Sun', [0,0], "yellow", 1.989*(10**21), [0,0], 25, 0, [0,0])   #Correct radius is 696340/(10**6), but changed to be more visual appeling
    
Mercury = Objects(planets_name[0], planets_pos[0], planets_color[0], planets_mass[0], planets_vel[0], planets_radius[0], planets_force[0], planets_momentum[0])
Venus = Objects(planets_name[1], planets_pos[1], planets_color[1], planets_mass[1], planets_vel[1], planets_radius[1], planets_force[1], planets_momentum[1])
Earth = Objects(planets_name[2], planets_pos[2], planets_color[2], planets_mass[2], planets_vel[2], planets_radius[2], planets_force[2], planets_momentum[2])
Mars = Objects(planets_name[3], planets_pos[3], planets_color[3], planets_mass[3], planets_vel[3], planets_radius[3], planets_force[3], planets_momentum[3])

#array with all plantes and sun

system = [Sun, Mercury, Venus, Earth, Mars]


# Using matplotlib to show the planets starting position

system_plot = []
for y, planets_3 in enumerate(system):
    system_plot.append(plt.Circle(system[y].pos, system[y].radius, color = system[y].color))
                  
plt.figure(dpi=1200)
plt.figure(1)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.set_xlim((-800, 800))
ax.set_ylim((-800, 800))
ax.set_facecolor('black')


for planets_4 in system_plot:
    ax.add_patch(planets_4)
    
    
# Calculating the effect the planets have on eachother due to gravity

plt.figure(dpi=1200)
plt.figure(2)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.set_xlim((-800, 800))
ax.set_ylim((-800, 800))
ax.set_facecolor('black')


time_max = 525949 * 100 #nummber of minutes in 100 years
time_max = 0.1
dt = 0.0000001
earth_pos = []

for time in range(1000):
    
    #Gives the forces each planets are effecting on eachother
    system[0].force = np.add(np.add(G_force(system[0], system[1]), G_force(system[0], system[2])), G_force(system[0], system[3]))
    system[1].force = np.add(np.add(G_force(system[1], system[0]), G_force(system[1], system[2])), G_force(system[1], system[3]))
    system[2].force = np.add(np.add(G_force(system[2], system[1]), G_force(system[2], system[0])), G_force(system[2], system[3]))
    system[3].force = np.add(np.add(G_force(system[3], system[1]), G_force(system[3], system[2])), G_force(system[3], system[0]))
    
    #Updates the momentom on each of the planets.
    
    system[0].momentum = system[0].momentum + system[0].force*dt
    system[1].momentum = system[1].momentum + system[1].force*dt
    system[2].momentum = system[2].momentum + system[2].force*dt
    system[3].momentum = system[3].momentum + system[3].force*dt
    
    #last step is to update the new position for this time step
    system[0].pos = system[0].pos + system[0].momentum/(system[0].mass*dt)
    system[1].pos = system[1].pos + system[1].momentum/(system[1].mass*dt)
    system[2].pos = system[2].pos + system[2].momentum/(system[2].mass*dt)
    system[3].pos = system[3].pos + system[3].momentum/(system[3].mass*dt)
    
    # plt.plot(system[1].pos, '*w')
    # plt.plot(system[2].pos, '--y')
    plt.plot(Earth.pos[0], Earth.pos[1],  '*g')
    
    

    earth_pos.append(Earth.pos)

# Using matplotlib to show the position of the planets after x amount of time.


system_plot_2 = []
for y, planets_3 in enumerate(system):
    system_plot_2.append(plt.Circle(list(system[y].pos), system[y].radius, color = system[y].color))



for planets_7 in system_plot_2:
    ax.add_patch(planets_7)
    

