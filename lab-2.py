import numpy as np
import math
#Question 1


my_arr = np.array([1,2,3,4])
print(my_arr[1])
print(my_arr[1:3])

my_arr[1] = 6
my_arr[2:3] = 42

my_arr = np.array([[1,2,3],[1,2,3]])
print(my_arr[1,2]) 

"""
first arg is the row, and second is the collum, or you can see it as
the first argument gives you the element in the "big list" and the second arguments
gives the element in the list that you got from the "big list"
"""

print(my_arr.shape)
print(my_arr.ndim) #dim = 0 = "scalar, dim = 1 = "vector", dim = 2 ="matrix"

print(my_arr.size) #gives total amount of elements including elements in the lists whitin lists
print(len(my_arr))  #gives the total elements in the "big list"/"top list"

#Question 2

matrix = np.random.random((10,10)) #the random values are distributed between 0 and 1
vector = np.ones(20)    #creates a vector with ones as each elements.
identity = np.identity(5) #Creates an identity matrix of shape NxN

#Question 3
A = np.random.random((4,4)) #Gives an 4x4 matrix with random numbers
B = np.random.random((4,4))

C = A + B	#Adds each value of each element between two matrix
C2 = np.add(A,B)   #Same as above but with different syntax

A2 = A + 6  #Adds 6 to each element in an matrix
B2 = B*2    #Double the value of each element in an matrix

#Question 4

Test = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(np.sum(Test))
print(np.min(Test))
print(np.matmul(Test,Test))
print(np.multiply(Test,Test))


#Question 5 - Slicing

Matrix_2 = np.random.random((10,10))
print(Matrix_2[0,0])
Matrix_2[9,9] = -1
print(Matrix_2[1,:]) #shows all values in the second row
print(Matrix_2[:,2]) #shows all values in collum 2 "third collum"
Matrix_2[1,:] = 0


#Question 6

def L2(vector):
    Total = 0
    for i in vector:
        Total = Total + i**2
        L2 = math.sqrt(Total)
    return  L2
        
vector = np.array([3,4]) # for any vector finds the L2 norm
print(L2(vector))
print(np.linalg.norm(vector))

#Question 7
Matrix_3 = np.random.random((10,10)) -0.5
New_Matrix_3 = np.where(Matrix_3 > 0,Matrix_3, Matrix_3*0)

#Question 8

R1 = np.random.random((10, 10))
R2 = R1 < 0.5  #gives an matrix where each value lower than 0.5 is true
print(R1)
print(R1[R2]) #prints all the values in R1 that is true, aka all values below 0.5
print(R1[~R2]) #prints all the values in R1 that is false, aka all values above 0.5
R1[R2] = -1
print(R1) #now prints the whole R1, where all the values that were true, aka below 0.5 are instead -1


