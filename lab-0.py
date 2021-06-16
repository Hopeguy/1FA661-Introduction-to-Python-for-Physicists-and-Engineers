import statistics
import math
#Lab 0

# given list of data
one_pulse = [1601, 1596, 1596, 1598, 1599, 1598, 1598, 1599, 1599, 1599,
             1594, 1586, 1572, 1550, 1525, 1503, 1489, 1482, 1479, 1475,
             1470, 1465, 1463, 1471, 1490, 1503, 1516, 1526, 1532, 1536, 
             1537, 1545, 1553, 1561, 1563, 1561, 1556, 1550, 1544, 1544, 
             1545, 1554, 1562, 1566, 1568, 1571, 1576, 1579, 1578, 1581, 
             1581, 1583, 1583, 1587, 1585, 1588]


#Q1 How many values are in this list? Print the result.

print(len(one_pulse))

#Q2 
#  print(one_pulse[100])  Gives an error as we dont have any values at index 100

#Q3
for i in one_pulse:
    print(i)

#---------------------Q4------------
total = 0
for i in one_pulse:
    total = total + i
    # or just use math.fsum(one_pulse)

print(total)    #total of all values added togehter
print(total/len(one_pulse)) #mean value

#----------------Q5-------------

def my_function(my_list):
    total = 0
    for i in my_list:
        total = total + i
    return total/len(my_list)

print(my_function(one_pulse))
print(statistics.mean(one_pulse))

# ----------------Q6 -------------------
print(one_pulse[-1])
print(one_pulse[0:9])
print(one_pulse[:5]) #gives the first 5 values in the lsit

print(my_function(one_pulse[0:10]))

# --------------Q7-----------------

print(max(one_pulse))
print(min(one_pulse))
one_pulse.sort()   #remove this to not get the list in order of lowest to highest
def numbers(your_list):
    high = max(your_list)
    low = min(your_list)
    middle = (high + low)/2

    
    for i in your_list:
        if i >= (high + middle)/2:
            print(i, ' is a high number')
        elif i <= (low + middle)/2:
            print(i, ' is a low number')
        else:
            print(i, ' is a middle number')

numbers(one_pulse)







