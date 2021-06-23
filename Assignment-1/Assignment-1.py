# Assignment 1 Joakim Ginste

"""
The section of this code loads the cvs file into python as an numpy array, and change 
the values to voltages through an equation shown below. As each voltage are taken at a specific time
with 5 nanoseconds inbetween an list with each timestep is also made.
An plot is lastly made using Voltage over time.
"""
import numpy
import matplotlib.pyplot as plt


# Question 1

pulses = numpy.loadtxt("pulses.csv", delimiter=',') # loads the excel file into pyton as an numpy array
print(pulses)

#Question 2
V_list = []
time = list(range(0,280,5)) #Creates a list for each of the 56 pulse elements, with step size of 5 to represent the 5 nanoseconds
for pulse in pulses:
    Voltages = pulse[1:] / (2**10 - 1) * 0.6 # changes the readings into voltages, not including the first element as that was only a timestamp
    V_list.append(Voltages)        # appends the calculated voltages into a list
    

#Question 3
plt.figure(1)
plt.plot(time, V_list[0], '--r') # uses the first row of voltage for simplicity to be plotted over the y axel, time on x axel in nanoseconds
plt.xlabel('Time [n seconds]')
plt.ylabel('Voltages [V]')
plt.title('Voltages over time')
plt.savefig("Voltages over time")
plt.show()


"""
This part calculates a baseline corrected values of the voltages using the mean value form
the first 10 elements of each pulse. This baseline corrected voltages are then ploted vs time 
as done in the segement before


Thereafter "maximum" values (in this case the biggest negative number) for each pulse is calculated
as well as the sum of all the elements in each pulse. These two new numbers are then plotted in
a histogram to be compared

"""

#Question 4
mean_constant = 10      #Constant to change the amount of elements to calculate the mean value from.
Corrected_Voltage = []  #Empty list that will be used to input the baselinecorrected values for the pulses.
for rows in V_list:    #goes thourgh each row of voltages
    Voltage_BL_corrected = rows - numpy.mean(rows[:mean_constant]) #Calculates the baseline corrected voltages for each pulse in an row
    Corrected_Voltage.append(Voltage_BL_corrected)  #list that adds the new baselin ecorrected row to a list, does this for each row to include all data.
    

#Question 5
plt.figure(2)
plt.plot(Corrected_Voltage[0], '--b') #also uses the first row of baseline corrected voltage to compare with the values of not baseline corrected
plt.xlabel('Time [n seconds]')
plt.ylabel('Voltages [V]')
plt.title('Voltages over time Baseline corrected')
plt.savefig("Voltages over time Baseline corrected")
plt.show()

#Question 6     

Max_values = []     #Empty list used to append the values into later
Total_pulse = []    
for Corrected_Pulse in Corrected_Voltage:   # Goes through each row ("pulse") from the baseline corrected values
    Max_values.append(numpy.min(Corrected_Pulse))   #finds the "maximum" values for each pulse and adds it to the list
    Total_pulse.append(numpy.sum(Corrected_Pulse))  #sums up all values from each pulse to one value and adds it to the list

plt.figure(3)
plt.hist(Max_values, bins = 100, color = 'r')    #plots a histogram over the max values for all 1000 pulses
plt.xlabel('Max value for each pulse')
plt.ylabel('Quantity')
plt.title('Histogram over max value for each pulse')
plt.savefig("Histogram over max value for each pulse")
plt.show()

plt.figure(4)
plt.hist(Total_pulse, bins = 100, color=('g'))  #plots a histogram over the summed values for each pulse for all pulses 
plt.xlabel("Total value of each pulse summed together")
plt.ylabel('Quantity')
plt.title('Histogram over total summed value for each pulse')
plt.savefig("Histogram over total summed value for each pulse")
plt.show()
    
    
    