import numpy as np
import matplotlib.pyplot as plt
import math
import time

#Question 1
arr1 = np.loadtxt(fname = "Ideal_Gas_Data.csv", skiprows=1, delimiter=",", dtype=str, usecols=range(1,11))
"""
skiprows skipes the first x rows of the input file
delimiter chooses at what type of character to divide into different elements
dtype = str makes all the values to strings instead of float values as standard
usecols gives what collums to be included, here an range is chosen where the first collume is removed, due to not being data but date

"""

#Question 2
# How many rows and columns does the array you created in question 1, have? Is this consistent with the input arguments and data?
# Yes as we have ten different rows of data as we have removed the "date" row

#Question 3

arr1_where_empty = arr1 ==''
arr1[arr1_where_empty] = np.nan

#Question 4
arr1_float = arr1.astype(float)
#the diffference between arr1, and arr1_float is that the latter is now in float values instead of strings

#Question 4.5 #gives same as arr1_float, but in one line
arr2 = np.genfromtxt(fname = "Ideal_Gas_Data.csv", dtype=float, delimiter= ',', usecols=range(1,11), skip_header=1)

#Question 5

plt.figure(1)
plt.plot(arr2[:,-1], arr2[:,1], '--b')
plt.title('Pressrue over Volume')
plt.ylabel('Pressure [kPa]')
plt.xlabel('Volume [$m^{3}$]')
plt.savefig('Pressure over time')

#Question 6
sin_array = np.arange(0, 2*math.pi)
sin_array_2 = np.linspace(0, 2*math.pi)

sin_array_new = []
for value in sin_array:
    sin_array_new.append(math.sin(value))

plt.figure(2)
plt.plot(sin_array_new, '--r') #bad plot as step size for sin_array is low and only have 7 elements

#Question 7

random_list = np.random.random(1000) #creates and list with 1000 elements
timestamp_before = time.time_ns()   #checks the times before the sort function is used on the array

random_list.sort()

timestamp_after = time.time_ns() #checks the time value after the sort function

differences_timestamp = timestamp_after - timestamp_before
print(differences_timestamp/10**9)  #prints the value of the difference between time to see how long time the sort function takes


#Question 8

x = np.array([0,1,2,3,4])   #here the array is written by hand, value where each point is 
y = np.array([0,1,2,3,4])

length = 25 #decides how many dots in each x and why
nx, ny = (length, length)       #assign the values of the total length to x and y
x = np.linspace(0,length,nx)    #creates an array with the start value of 0 and length and last value as the same value
y = np.linspace(0,length,ny)
xv, yv = np.meshgrid(x,y)   #creates the x and y values for an meshgrid

plt.figure(3)
plt.plot(xv, yv, marker='.', color='k', linestyle='none') #prints the values for the meshgrids x and y

