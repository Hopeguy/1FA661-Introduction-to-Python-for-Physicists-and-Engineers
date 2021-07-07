
'''
Project solar system

Joakim Ginste

# '''

import turtle as tl
import numpy as np
import matplotlib.pyplot as plt
import time


# win = tl.Screen()
# win.title('Solar system')
# win.bgcolor('black')

# earth = tl.Turtle()
# earth.shape('circle')
# earth.color('green', 'blue')

# while True:
    
#     earth.forward(2)
#     time.sleep(0.01)
#     earth.left(2)
#     earth.forward(2)
#     time.sleep(0.01)
#     earth.left(2)
#     earth.forward(2)
#     time.sleep(0.01)
#     earth.left(2)
    
#     earth.penup()
#     earth.forward(20)
#     earth.pendown()
    

# win.mainloop()

# tl.done()



# def G_force(planet1,planet2): # calculats the garvitaional force exerted on p1 by p2

#     G = 6.67*10**-11 # Gravitional constant
    
#     r_vec = planet1.pos-planet2.pos # calculates the distance vector between p1 and p2
    
#     r_mag = mag(r_vec) # gives magnitude of the distance vector
    
#     r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
#     force_mag = G*planet1.mass * planet2.mass / (r_mag**2) # gives force magnitude

#     force_vec = -force_mag*r_hat # gives force vector 
    
#     return force_vec #Output force 1 by 2

# e_graph = gcurve(color=color.blue)
# def gforce(p1,p2):
#     # Calculate the gravitational force exerted on p1 by p2.
#     G = 1 # Change to 6.67e-11 to use real-world values.
#     # Calculate distance vector between p1 and p2.
#     r_vec = p1.pos-p2.pos
#     # Calculate magnitude of distance vector.
#     r_mag = mag(r_vec)
#     # Calcualte unit vector of distance vector.
#     r_hat = r_vec/r_mag
#     # Calculate force magnitude.
#     force_mag = G*p1.mass*p2.mass/r_mag**2
#     # Calculate force vector.
#     force_vec = -force_mag*r_hat
    
#     return force_vec
    
# star = sphere( pos=vector(0,0,0), radius=0.2, color=color.yellow,
#                mass = 1000, momentum=vector(0,0,0), make_trail=True )
               
# planet1 = sphere( pos=vector(1,0,0), radius=0.05, color=color.blue,
#                   mass = 1, momentum=vector(0,30,0), make_trail=True )

# planet2 = sphere( pos=vector(0,3,0), radius=0.075, color=color.red,
#                   mass = 2, momentum=vector(-35,0,0), make_trail=True )
                  
# planet3 = sphere( pos=vector(0,-4,0), radius=0.1, color=color.green,
#                   mass = 10, momentum=vector(160,0,0), make_trail=True )
               
# dt = 0.0001
# t = 0
# while (True):
#     rate(1000)
    
#     # Calculate forces.
#     star.force = gforce(star,planet1)+gforce(star,planet2)+gforce(star,planet3)
#     planet1.force = gforce(planet1,star)+gforce(planet1,planet2)+gforce(planet1,planet3)
#     planet2.force = gforce(planet2,star)+gforce(planet2,planet1)+gforce(planet2,planet3)
#     planet3.force = gforce(planet3,star)+gforce(planet3,planet1)+gforce(planet3,planet2)

#     # Update momenta.
#     star.momentum = star.momentum + star.force*dt
#     planet1.momentum = planet1.momentum + planet1.force*dt
#     planet2.momentum = planet2.momentum + planet2.force*dt
#     planet3.momentum = planet3.momentum + planet3.force*dt

#     # Update positions.
#     star.pos = star.pos + star.momentum/star.mass*dt
#     planet1.pos = planet1.pos + planet1.momentum/planet1.mass*dt
#     planet2.pos = planet2.pos + planet2.momentum/planet2.mass*dt
#     planet3.pos = planet3.pos + planet3.momentum/planet3.mass*dt
    
#     t = t + dt


# Attempt 1

#----------Class objects-----------

class Objects:
    def __init__(self, name, pos, color, mass, in_vel, radius):
        self.name = name
        self.pos = pos
        self.color = color
        self.mass = mass
        self.in_vel = in_vel #initial velocity
        self.radius = radius



#---------Functions--------

def G_force(planet1,planet2): # calculats the garvitaional force exerted on p1 by p2

    G = 6.67*10**-11 # Gravitional constant
    
    r_vec = planet1.pos-planet2.pos # calculates the distance vector between p1 and p2
    
    r_mag = np.linalg.norm(r_vec) # gives magnitude of the distance vector
    
    r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
    force_mag = G*planet1.mass * planet2.mass / (r_mag**2) # gives force magnitude

    force_vec = -force_mag*r_hat # gives force vector 
    
    return force_vec #Output force 1 by 2


def set_parameters(name, position, shape, color, radius):
    name = tl.Turtle()
    name.setpos(position)
    name.color(color)    
    name.shape(shape)
    name.shapesize(radius,radius,radius)
    

# #----------Turtle Objects-------

win = tl.Screen()
win.title('Solar system')
win.bgcolor('black')




# Data and for loop for planets

#take form https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 


planets_name = ['Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planets_pos = ([[57.9,0], [108.2,0], [149.6,0], [149.984,0], [227.9,0], [778.6,0], [1433.5,0], [2872.5,0], [4495.1,0], [5906.4,0]])  # * 10**6 km, same y value as they are starting on a line "distance from sun"
planets_color = ['grey', 'orange', 'green', 'grey', 'yellow', 'yellow', 'yellow', 'cyan', 'blue', 'grey']
planets_mass = [0.330, 4.87, 5.97, 0.073, 0.642, 1898, 568, 86.8, 102, 0.0146] #mass in kg /(10**24)
planets_vel = [[47.4, 0], [35.0, 0], [29.8, 0], [1.0, 0], [24.1, 0], [13.1, 0], [9.7, 0], [6.8, 0],	[5.4, 0], [4.7, 0]] #km/s "orbital velocity"
planets_radius = [4879,	12104,	12756,	3475,	6792,	142984,	120536,	51,118,	49528,	2370] #diameter in km

for i, planet in enumerate(planets_pos):  #reduces starting distance from sun to be able to see all planets in the window.
    planets_pos[i] = [planet[0]/10, planet[1]]

for k, planet_2 in enumerate(planets_radius):
    planets_radius[k] = planet_2/(2*10**6)
    
Mercury = Objects(planets_name[0], planets_pos[0], planets_color[0], planets_mass[0], planets_vel[0], planets_radius[0])
Venus = Objects(planets_name[1], planets_pos[1], planets_color[1], planets_mass[1], planets_vel[1], planets_radius[1])
Earth = Objects(planets_name[2], planets_pos[2], planets_color[2], planets_mass[2], planets_vel[2], planets_radius[2])
Moon = Objects(planets_name[3], planets_pos[3], planets_color[3], planets_mass[3], planets_vel[3], planets_radius[3])
Mars = Objects(planets_name[4], planets_pos[4], planets_color[4], planets_mass[4], planets_vel[4], planets_radius[4])
Jupiter = Objects(planets_name[5], planets_pos[5], planets_color[5], planets_mass[5], planets_vel[5], planets_radius[5])
Saturn = Objects(planets_name[6], planets_pos[6], planets_color[6], planets_mass[6], planets_vel[6], planets_radius[6])
Uranus = Objects(planets_name[7], planets_pos[7], planets_color[7], planets_mass[7], planets_vel[7], planets_radius[7])
Neptune = Objects(planets_name[8], planets_pos[8], planets_color[8], planets_mass[8], planets_vel[8], planets_radius[8])
Pluto = Objects(planets_name[9], planets_pos[9], planets_color[9], planets_mass[9], planets_vel[9], planets_radius[9])


Sun = Objects('Sun', [0,0], "yellow", 1.989*6, [0,0], 696340/(10**6))   

#array with all plantes and sun

system = [Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
#Turtle setup

for t in system:
    set_parameters(t.name, t.pos, 'circle', t.color, t.radius)



win.mainloop()
win.done()