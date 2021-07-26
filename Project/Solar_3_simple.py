import numpy as np
import matplotlib.pyplot as plt



# Attempt 1

#----------Class objects-----------

class Objects:
    def __init__(self, name, pos, color, mass, vel, radius, acc):
        self.name = name
        self.pos = np.array(pos)
        self.color = color
        self.mass = mass
        self.vel = np.array(vel) #initial velocity
        self.radius = radius
        self.acc = np.array(acc)
        
#---------Global Constants------------

G = 6.67*10**-11 # Gravitional constant   
lim_fig = 5*10**11
year_min = 8760 #hours in a year
    

#---------Functions--------

def Acc(planet1,planet2): # calculats the gravitaional force exerted on p1 by p2 by their distances from eachother. sun is at 0
    
    r_vec = np.subtract(planet1.pos, planet2.pos)# calculates the distance vector between p1 and p2
    
    r_mag = np.linalg.norm(r_vec) # gives magnitude of the distance vector
    
    r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
    acc = -((G*planet2.mass) / (r_mag**2))*r_hat # gives the new acceleration of p1 from the force of p2
    
    return acc #Output new acceleration 


# Data for planets

#take form https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 

#pos = Distance from sun (an average distance over one orbit), all planets starting on the x axis with y = 0
#vel = Orbital velocity, starts as an vector staright up in y direction, as all planets starts on a line on the x axis.
 
#all data is given in SI units
Sun = Objects('Sun', [0,0], "yellow", 1.989*(10**30), [0,0], 0.25*10**11, [0,0])
Earth = Objects('Earth', [149.6*10**9,0], 'green', 5.97*10**24, [0, 29.8*10**3], 0.1*10**11, [0,0])


#array with all plantes and sun

system = [Sun, Earth]

# Using matplotlib to show the planets starting position

system_plot = []
for y, planet in enumerate(system):
    system_plot.append(plt.Circle(system[y].pos, system[y].radius, color = system[y].color))

plt.figure(1, dpi = 1200)             

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.set_xlim((-lim_fig, lim_fig))
ax.set_ylim((-lim_fig, lim_fig))
ax.set_facecolor('black')


for planets_5 in system_plot:
    ax.add_artist(planets_5)


plt.show
    
#---------Now we calculate how the planets/sun effects eachother

time_max = year_min #nummber of minutes in 100 year (times 100)

dt = 3600  # we work in SI units, so with time step of 1 hour per step
earth_pos = np.zeros((time_max, 2))
earth_vel = np.zeros((time_max, 2))
earth_acc = np.zeros((time_max, 2))

print(Earth.pos)


#Intergration using forward and backward differentiation

for i in range(time_max):
    
    #Calculates the accelration the planet experience during this minute
    Earth.acc = Acc(Earth, Sun)
    
    #Updates the position of the planet depending on the velocity it currently have and the time step (forward differentiation)
    
    Earth.pos += (np.array(Earth.vel)*dt)
    
    #last step is to update the velocity with the help of the acceleration and time step (backward differentiation)
  
    Earth.vel += (np.array(Earth.acc) * dt)
    

    earth_pos[i] = Earth.pos
    earth_vel[i] = Earth.vel
    earth_acc[i] = Earth.acc


#Intergration using Verlet-leapfrog predictor as recommended by: http://nbabel.org/equations

# acc_stored = np.array([[0,0],[0,0]])

# for i in range(time_max):
    
#     #Calculates the accelration the planet experience during this minute
#     Earth.acc = Acc(Earth, Sun)
#     acc_stored = [acc_stored[1], Earth.acc]
    
#     #Updates the position of the planet depending on the velocity it currently have and the time step
    
#     Earth.pos += (Earth.vel*dt) + 0.5*(Earth.acc)*(dt**2)
    
#     #last step is to update the velocity with the help of the acceleration and time step
  
#     Earth.vel += 0.5 * (acc_stored[0] + acc_stored[1]) * dt
    
#     #Stores the position points to be used for plotting.
#     earth_pos[i] = Earth.pos


# Using matplotlib to show the position of the planets after x amount of time.

        
plt.figure(dpi = 1200)
fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.set_xlim((-lim_fig, lim_fig))
ax.set_ylim((-lim_fig, lim_fig))
ax.set_facecolor('black')  
    
plt.plot(earth_pos[:,0], earth_pos[:,1], '--g')

print(Earth.pos)

system_plot_2 = []
for t, planets_6 in enumerate(system):
    system_plot_2.append(plt.Circle(list(system[t].pos), system[t].radius, color = system[t].color))

for planets_7 in system_plot_2:
    ax.add_artist(planets_7)


