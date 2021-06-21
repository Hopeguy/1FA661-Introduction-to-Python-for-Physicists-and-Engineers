# Lab-1
import math
import matplotlib.pyplot as plt

#Q1
print("---------Question 1----------")
with open ("Ideal_Gas_Data.csv", 'r') as inputfile:
    print(inputfile.readline())  # the r stands for "open for reading"


#Q2
print("------Question 2---------")
f = open("Ideal_Gas_Data.csv", 'r')
lines = f.readlines()
for line in lines[1:]:          #for loops that iteratios over the csv file but not the first value
    splitline = line.split(",") #splits each line in the for loop to make a list of each line
    print(splitline[2])         #prints out the 3 index value aka pressure form the lines.
    
#Q3
print("------Question 3 ----------")
times = []
pressures_abs = []
temps = []
volumes = []
    

f = open("Ideal_Gas_Data.csv", 'r')
lines = f.readlines()
for line in lines[1:]:  #Fills the list with the right values
    splitlines = line.split(',')    
    times.append(splitlines[1])
    pressures_abs.append(splitlines[2])
    temps.append(splitlines[3])
    volumes.append(splitlines[-1])
    pass

#Q4 
print("---------Question 4---------")
def stringtofloat(List, index): #funciton the takes an list and an index to make a list of the values of that index
    return_list = []
    for line in List[1:]:
        splitlines = line.split(',') # split the line into its own list
        float_num = float(splitlines[index])    #change the value at index in the list to a float number from str
        return_list.append(float_num)   #appends the float value into the list that will get returned from the funciton

    return return_list


f = open("Ideal_Gas_Data.csv", 'r')
lines = f.readlines()

print(stringtofloat(lines,2)) # prints out the list from the file at a specific index value 2 = pressure


#Q5,Q6,Q7       many different plots
font = {'family': 'serif',  #choose of font
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

temps = stringtofloat(lines,3)
plt.plot(temps, '_:r')
plt.grid(True)      #adds a grid to the plot
plt.title("temps depending on time", fontdict=font) #adds a title to the plot
plt.xlabel('Index(time)')
plt.ylabel('Temp(Celcius)')
plt.show

#Q8
volumes = stringtofloat(lines,-1)
pressure = stringtofloat(lines,2)
times = stringtofloat(lines,1)

plt.figure(1)
plt.plot(times, volumes, '--b', label = 'Volume [$m^{3}$]')
plt.plot(times, pressure, '--r', label = 'Pressure[kPa]')
plt.plot(times, temps, '--g', label = 'Temperature[$^\circ$C)]')
plt.legend()
plt.title('stuff depending on time')
plt.xlabel('time [s]')
plt.ylabel('Temp, Pressure and Volume')

plt.savefig("plot of time dependence")      #saves the plot as an png file

#Q9
plt.figure(2) 
plt.plot(volumes, pressure, '--b')
plt.title("pressure over volume")
plt.xlabel('Volume [$m^{3}$]')
plt.ylabel('Pressure [kPa]')

plt.savefig("Pressure over Volume")


#Q10

plt.figure(3)
fig, axs = plt.subplots(3, sharex=True, sharey=False) #makes 3 subplots where they share the same x axis
fig.suptitle('Stuff depending on time') #it is supposed to say suptitle, to get an common title for the subplots!!
axs[0].plot(times, volumes, '--b', label = 'Volume [$m^{3}$]')
axs[1].plot(times, pressure, '--r', label = 'Pressure[kPa]')
axs[2].plot(times, temps, '--g', label = 'Temperature[$^\circ$C)]')
plt.savefig("subplott stuff over time")
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html #for more plots