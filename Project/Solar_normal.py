'''
Project solar system

Joakim Ginste

# '''
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
Accuracy_const = 30 # at 30 we change from a step size of hours to 2 minutes, The higher accuracy number the lower the step size
time_max = int(8760*Accuracy_const) * 100 #Minutes in a Earth year if Accuracy constants = 60 * times 100 years
    

#---------Functions--------

def Acc(planet1,planet2): # calculats the new acceleration on p1 by the effects of p2 by their distances from eachother. sun is at 0
    
    r_vec = np.subtract(planet1.pos, planet2.pos)# calculates the distance vector between p1 and p2
    
    r_mag = np.linalg.norm(r_vec) # gives magnitude of the distance vector
    
    r_hat = r_vec/r_mag # gives the unit vector of the distance vector
    
    acc = -((G*planet2.mass) / (r_mag**2))*r_hat # gives the new acceleration vector of p1 from the force of p2
  
    return acc #Output new acceleration 


#-------------Setup of solar system--------------------

# Data for planets taken form https://nssdc.gsfc.nasa.gov/planetary/factsheet/ 

#pos = Distance from sun (an average distance over one orbit), all planets starting on the x axis with y = 0
#vel = Orbital velocity, starts as an vector staright up in y direction, as all planets starts on a line on the x axis.
 
#all data is given in SI units
Sun = Objects('Sun', [0,0], "yellow", 1.989*(10**30), [0,0], 0.25*10**11, [0,0])

Mercury = Objects('Mercury', [57.9*10**9,0], 'gray', 0.330*10**24, [0, 47.4*10**3], 0.1*10**11, [0,0])
Venus = Objects('Venus', [108.2*10**9,0], 'magenta', 4.87*10**24, [0, 35*10**3], 0.1*10**11, [0,0])
Earth = Objects('Earth', [149.6*10**9,0], 'green', 5.97*10**24, [0, 29.8*10**3], 0.1*10**11, [0,0])
Mars = Objects('Mars', [227.9*10**9,0], 'Red', 0.642*10**24, [0, 24.1*10**3], 0.3*10**11, [0,0])
Jupiter = Objects('Jupiter', [778.6*10**9,0], 'darkorange', 1898*10**24, [0, 13.1*10**3], 1*10**11, [0,0])
Saturn = Objects('Saturn', [1433.5*10**9,0], 'orange', 568*10**24, [0, 9.7*10**3], 1*10**11, [0,0])
Uranus =  Objects('Uranus', [2872.5*10**9,0], 'lightsteelblue', 86.8*10**24, [0, 6.8*10**3], 1*10**11, [0,0])
Neptune = Objects('Neptune', [4495.1*10**9,0], 'lightblue', 102*10**24, [0, 5.4*10**3], 1*10**11, [0,0])

#no pluto as it is not considered a planet 

system = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune] #array with all plantes and sun


    
#---------Calculations of how the planets/sun effects eachother----------------

dt = 3600/Accuracy_const  # we work in SI units, so with timestep of 2 minute per step if accuracy_constant = 30

# List to store the positions of the planets for plotting
Sun_pos = np.zeros((time_max, 2)) 
Mercury_pos = np.zeros((time_max, 2))
Venus_pos = np.zeros((time_max, 2))
Earth_pos = np.zeros((time_max, 2))
Mars_pos = np.zeros((time_max, 2))
Jupiter_pos = np.zeros((time_max, 2))
Saturn_pos = np.zeros((time_max, 2))
Uranus_pos = np.zeros((time_max, 2))
Neptune_pos = np.zeros((time_max, 2))



for time in range(time_max): #main equation for solving the orbits/paths over 100 years
    
    #Calculates the accelration the planet experience during this minute
    for planet in system[1:]: #going through the new acc on each planet due to the other bodies
        planet_store = [planet.acc,0]
        planet.acc =[0,0]
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
        
        #Stores the position points to be used for plotting.
        
    Mercury_pos[time] = Mercury.pos
    Venus_pos[time] = Venus.pos
    Earth_pos[time] = Earth.pos
    Mars_pos[time] = Mars.pos
    Jupiter_pos[time] = Jupiter.pos
    Saturn_pos[time] = Saturn.pos
    Uranus_pos[time] = Uranus.pos
    Neptune_pos[time] = Neptune.pos
    Sun_pos[time] = Sun.pos
    


#--------------Using matplotlib to show the planets starting position-------------
Starting_system = [Mercury_pos[0], Venus_pos[0], Earth_pos[0], Mars_pos[0], Jupiter_pos[0], Saturn_pos[0],  Uranus_pos[0],  Neptune_pos[0]]

system_plot = []
for y, planet_plot in enumerate(Starting_system):
    system_plot.append(plt.Circle(Starting_system[y], system[y].radius, color = system[y].color, label = system[y].name)) 

fig1, ax1 = plt.subplots() 

ax1.set_xlim((-lim_fig, lim_fig))
ax1.set_ylim((-lim_fig, lim_fig))
ax1.set_facecolor('black')


for f, planets_5 in enumerate(system_plot):
    ax1.add_patch(planets_5)

plt.legend()
plt.title("Solar system starting position")
plt.xlabel("[m]")
plt.ylabel("[m]")

fig1.savefig("Images/Starting positions for solar system.png")


#----------------Plotting of the paths the planets over 100 years---------------
        
fig2, ax2 = plt.subplots() 

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


plt.legend()
plt.title("Solar system with extra star after 100 years")
plt.xlabel("[m]")
plt.ylabel("[m]")

system_plot_2 = []
for t, planets_6 in enumerate(system):
    system_plot_2.append(plt.Circle(list(system[t].pos), system[t].radius, color = system[t].color))

for planets_7 in system_plot_2:
    ax2.add_artist(planets_7)

fig2.savefig("Images/solar system after 100 years.png")














