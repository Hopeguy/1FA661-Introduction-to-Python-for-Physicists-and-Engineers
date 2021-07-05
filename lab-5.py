
#-------------LAB 5 probability and simulations-------------

import numpy as np
import matplotlib.pyplot as plt

#--------------Question 1

rand_arr = np.random.randint(1,7) #returns an interger between 1-6

#----------Question 2----------

N = 10000
rolls = np.random.randint(1,7,N)
dist = np.zeros(6)

for i in range(N):
    if rolls[i] == 1:
        dist[0] += 1
    elif rolls[i] == 2:
        dist[1] += 1
    elif rolls[i] == 3:
        dist[2] += 1
    elif rolls[i] == 4:
        dist[3] += 1
    elif rolls[i] == 5:
        dist[4] += 1
    elif rolls[i] == 6:
        dist[5] += 1
         
        
#--------------Question 3--------------

dist2 = np.histogram((rolls),bins = range(1,8))

#----------Question 4---------
plt.figure(1)
plt.bar(range(1,7), dist2[0])
plt.title('Distribution of 6-sided dice rollings, n=10,000')

#------------Question 5-----------------

def dice_rolls(N,M):        #function that gets the summed up rolls of M dices using N rolls
    dice_rolls = np.zeros((M,N))
    for dice in range(M):
        dice_rolls[dice] = np.random.randint(1,7,N)
    
    summed_rolls = np.zeros(N)
    for roll in range(N):
        summed_rolls[roll] = sum(dice_rolls[:,roll]) 
        
    return summed_rolls     #output is an N Array with the summed values from the M dices

N = 10000 #Number of rolls
M = 5 #Number of dices (regular 1-6 dices)

print(dice_rolls(N, M))

dist3 = np.histogram(dice_rolls(N,M), bins = range(1,(6*M)+2)) #gets the distribution using histogram
plt.figure(2)
plt.bar(range(1,(6*M)+1),dist3[0])  #plots a bar plot


#------------Question 6 --------------

N = 1000

ran_pair = np.stack([np.random.random(N), np.random.random(N)])
inside = 0
outside = 0

plt.figure(4)
for points in range(N): #solves if an point is inide or outside and plots it depending on that with different colours
    if np.linalg.norm(ran_pair[:,points]) <= 1:
        inside += 1
        plt.plot(ran_pair[0,points], ran_pair[1,points], '.r')
    
    else:
        outside += 1
        plt.plot(ran_pair[0,points], ran_pair[1,points], '.g')
        


theta = np.linspace(0,0.5*np.pi,100)
r = np.sqrt(1)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
plt.plot(x1, x2, '-')  #plots the quarther circle
    
pi = 4*(inside/(N))
print(pi)



