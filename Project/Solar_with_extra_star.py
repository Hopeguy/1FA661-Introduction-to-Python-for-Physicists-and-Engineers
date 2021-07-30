
import numpy as np
import matplotlib.pyplot as plt

#----------Class objects-----------

class Objects:
    def __init__(self, name, pos, color, mass, vel, radius, acc):
        self.name = name
        self.pos = np.array(pos)
        self.color = color
        self.mass = mass
        self.vel = np.array(vel) #initial velocity
        self.radius = np.array(radius)
        self.acc = np.array(acc)
        
#---------Global Constants------------

G = 6.67*10**-11 # Gravitional constant   
lim_fig = 5*10**12  #Sets the limits on the plot figures
plt.rcParams['figure.figsize'] = (16*2,9*2) #changes the aspect ratio and size of the plots to 16:9
Accuracy_const = 10 # at 10 we change from a step size of hours to 6 minutes, The higher the value the lower step size used
time_max = int(8760*Accuracy_const) * 100 #Minutes in a Earth year if Accuracy constants = 60 * times 100 years
    
    

#---------Functions--------

def Acc(planet1,planet2): # calculats the new acceleration on p1 by the effects of p2 by their distances from eachother. sun is at 0
    
    r_vec = np.subtract(planet1.pos, planet2.pos)# calculates the distance vector between p1 and p2
    
    r_mag = np.linalg.norm(r_vec) # gives magnitude of the distance vector
    
    r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
    acc = -((G*planet2.mass) / (r_mag**2))*r_hat # gives the new acceleration vector of p1 from the force of p2
  
    return acc #Output new acceleration 


# Data for planets

#take form https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 

#pos = Distance from sun (an average distance over one orbit), all planets starting on the x axis with y = 0
#vel = Orbital velocity, starts as an vector staright up in y direction, as all planets starts on a line on the x axis.
#radius = is not the acctual radius, as then it would not be possible to see the smaller planets
 
#all data is given in SI units
Sun = Objects('Sun', [0,0], "yellow", 1.989*(10**30), [0,0], 0.3*10**11, [0,0])

Mercury = Objects('Mercury', [57.9*10**9,0], 'gray', 0.330*10**24, [0, 47.4*10**3], 0.1*10**11, [0,0])
Venus = Objects('Venus', [108.2*10**9,0], 'magenta', 4.87*10**24, [0, 35*10**3], 0.1*10**11, [0,0])
Earth = Objects('Earth', [149.6*10**9,0], 'green', 5.97*10**24, [0, 29.8*10**3], 0.1*10**11, [0,0])
Mars = Objects('Mars', [227.9*10**9,0], 'Red', 0.642*10**24, [0, 24.1*10**3], 0.3*10**11, [0,0])
Jupiter = Objects('Jupiter', [778.6*10**9,0], 'pink', 1898*10**24, [0, 13.1*10**3], 0.3*10**11, [0,0])
Saturn = Objects('Saturn', [1433.5*10**9,0], 'orange', 568*10**24, [0, 9.7*10**3], 0.3*10**11, [0,0])
Uranus =  Objects('Uranus', [2872.5*10**9,0], 'lightsteelblue', 86.8*10**24, [0, 6.8*10**3], 0.3*10**11, [0,0])
Neptune = Objects('Neptune', [4495.1*10**9,0], 'lightblue', 102*10**24, [0, 5.4*10**3], 0.3*10**11, [0,0])

#no pluto as it is not an planet 

#array with all plantes and sun

#---------------Extra star part---------------

'''
Firstly an calculation is made to find the length of the solar system by using Neptunes orbit diameter

Thereafter a random spot on a orbit of Neptune, is calculated.
with the help of the "length" of the solar system and the timeframe of
100 years we can find the required velocity of the extra star to make it through
in 100 years.

With the random spot the velocity vector can be found in order to assure that
the Star will be as close to the sun as the earth is.

There will also be 4 different cases for how the velocity are defined depending
on what quadrant of the elipps that the star starts in
'''
angle = np.random.uniform(-np.pi, np.pi)

Star = Objects("Star", [np.cos(angle)*Neptune.pos[0], np.sin(angle)*Neptune.pos[0]], "white", Sun.mass, [0, 0], 0.3*10**11, [0,0])

alpha_v = np.arctan(Earth.pos[0]/Neptune.pos[0])
system_length = Neptune.pos[0]*2  #as the "distance from sun" times two of the planet farthest out gives the solar system length
Star_vel = system_length/(100*8760*3600) #length/time, just gives the magnitude.


if Star.pos[0] > 0 and Star.pos[1] > 0: #checks for what quadrant and fix the velocity vector to go close to the sun
    
    beta_v = np.arctan(Star.pos[0]/Star.pos[1])
    alpha_x = -(np.pi/2) - alpha_v - beta_v
    
elif Star.pos[0] > 0 and Star.pos[1] < 0:
  
    beta_v = np.arctan(Star.pos[0]/Star.pos[1])
    alpha_x = (np.pi/2) - alpha_v - beta_v
        
elif Star.pos[0] < 0 and Star.pos[1] < 0:
    
    beta_v = np.arctan(Star.pos[0]/Star.pos[1])
    alpha_x = (np.pi/2) - alpha_v - beta_v
    
elif Star.pos[0] < 0 and Star.pos[1] > 0:
  
    beta_v = np.arctan(Star.pos[0]/Star.pos[1])
    alpha_x = -(np.pi/2) - alpha_v - beta_v
  
vel_x = Star_vel*np.cos(alpha_x)
vel_y = Star_vel*np.sin(alpha_x)
Star.vel = np.array([vel_x, vel_y])

Star_pos_start = np.zeros((time_max, 2))
Star_save_pos = Star.pos #saves the stars starting position as it will be changed when creating the predicted path
Star_save_vel = Star.vel
Starting_system = [Sun.pos, Mercury.pos, Venus.pos, Earth.pos, Mars.pos, Jupiter.pos, Saturn.pos,  Uranus.pos,  Neptune.pos, Star.pos]

dt_start = 3600

for time_start in range(time_max):  #Gives the data to print the projected path of the incoming start into the solar system
    
    Star_pos_start[time_start] = Star.pos 
     
    #Updates the position of the planet depending on the velocity it currently have and the time step
    Star.pos = Star.pos + Star.vel*dt_start    
    
Star.pos = Star_save_pos #returns the saved starting value before the real simulation


system = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Star] #Creats an array with all the planets/stars in them

    
#---------Calculate of how the planets/sun effects eachother-----------------

dt = 3600/Accuracy_const # we work in SI units, so with time  step of 6 minute per step

# Lists to store the positions of the planets for plotting later on

Sun_pos = np.zeros((time_max, 2))
Mercury_pos = np.zeros((time_max, 2))
Venus_pos = np.zeros((time_max, 2))
Earth_pos = np.zeros((time_max, 2))
Mars_pos = np.zeros((time_max, 2))
Jupiter_pos = np.zeros((time_max, 2))
Saturn_pos = np.zeros((time_max, 2))
Uranus_pos = np.zeros((time_max, 2))
Neptune_pos = np.zeros((time_max, 2))
Star_pos = np.zeros((time_max, 2))

for time in range(time_max): #main equation for solving the orbits/paths over 100 years
    
    #Calculates the accelration the planet experience during this timestep
    for planet in system: #going through the new acc on each planet due to the other bodies
        planet_store = [planet.acc,0]
        planet.acc = np.array([0,0])
        for planet_eff in system: #goes through all the planets and adds their gravitational effect on the planet we are calculating the total new acc on.
            if planet != planet_eff: #this makes sure so the planet does not try to include its own effect on itself
                planet.acc = np.add(planet.acc, Acc(planet, planet_eff)) 
                
            else:
                    pass
            
        planet_store[1] = planet.acc
            
        #Updates the position of the planet depending on the velocity it currently have and the time step
        planet.pos = planet.pos + planet.vel*dt + 0.5*planet.acc*(dt**2)
            
        #last step is to update the velocity with the help of the acceleration and time step
            
        planet.vel = planet.vel + 0.5*(planet_store[0] + planet_store[1])*dt
        
    #Stores the position points at each timestep to be used for plotting.
        
    Mercury_pos[time] = Mercury.pos
    Venus_pos[time] = Venus.pos
    Earth_pos[time] = Earth.pos
    Mars_pos[time] = Mars.pos
    Jupiter_pos[time] = Jupiter.pos
    Saturn_pos[time] = Saturn.pos
    Uranus_pos[time] = Uranus.pos
    Neptune_pos[time] = Neptune.pos
    Star_pos[time] = Star.pos
    Sun_pos[time] = Sun.pos
    
    
#---------Using matplotlib to show the planets starting position, with Star and its projected path-------------

            
fig1, ax1 = plt.subplots() #uses subplots to be able to print Circles

ax1.set_xlim((-lim_fig, lim_fig))
ax1.set_ylim((-lim_fig, lim_fig))
ax1.set_facecolor('black')

plt.plot(Star_pos_start[:,0], Star_pos_start[:,1], color = Star.color, linestyle=':') #prints the predicted path of the Star through the solar system
system_plot = [] #empty list to store the Circle patch for each planet

for y, planet_plot in enumerate(Starting_system): #creates a circle for each planet, sun and star
    system_plot.append(plt.Circle(Starting_system[y], system[y].radius, color = system[y].color, label = system[y].name))
    

for f, planets_5 in enumerate(system_plot): #used to print the circles to the plot
    ax1.add_patch(planets_5)


plt.legend()
plt.title("Solar system starting position with Star and its projected path")
plt.xlabel("[m]")
plt.ylabel("[m]")

fig1.savefig("Images/Starting position at year Zero with extra star and projected path.png")


#---------------Plotting of the paths the planets/Star takes----------------
     

plt.rcParams['figure.figsize'] = (16*2,9*2)
fig2, ax2 = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax2.set_xlim((-lim_fig, lim_fig))
ax2.set_ylim((-lim_fig, lim_fig))
ax2.set_facecolor('black')  
  
plt.plot(Sun_pos[:,0], Sun_pos[:,1], color = Sun.color, linestyle=':', label = Sun.name)  
plt.plot(Mercury_pos[:,0], Mercury_pos[:,1], color = Mercury.color, linestyle=':', label = Mercury.name)
plt.plot(Venus_pos[:,0], Venus_pos[:,1], color = Venus.color, linestyle=':', label = Venus.name)
plt.plot(Earth_pos[:,0], Earth_pos[:,1], color = Earth.color, linestyle=':', label = Earth.name)
plt.plot(Mars_pos[:,0], Mars_pos[:,1], color = Mars.color, linestyle=':', label = Mars.name)
plt.plot(Jupiter_pos[:,0], Jupiter_pos[:,1], color = Jupiter.color, linestyle=':', label = Jupiter.name)
plt.plot(Saturn_pos[:,0], Saturn_pos[:,1], color = Saturn.color, linestyle=':', label = Saturn.name)
plt.plot(Uranus_pos[:,0], Uranus_pos[:,1], color = Uranus.color, linestyle=':', label = Uranus.name)
plt.plot(Neptune_pos[:,0], Neptune_pos[:,1], color = Neptune.color, linestyle=':', label = Neptune.name)
plt.plot(Star_pos[:,0], Star_pos[:,1], color = Star.color, linestyle=':', label = Star.name)

plt.legend()
plt.title("Solar system with extra star after 100 years")
plt.xlabel("[m]")
plt.ylabel("[m]")


system_plot_2 = []
for t, planets_6 in enumerate(system):
    system_plot_2.append(plt.Circle(list(system[t].pos), system[t].radius, color = system[t].color))

for planets_7 in system_plot_2:
    ax2.add_patch(planets_7)


fig2.savefig("Images/Solar system with extra star after 100 years.png")

print(Star_save_vel)








