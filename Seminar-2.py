
#Fibbonaci seq

import numpy as np
import matplotlib.pyplot as plt

fib = np.array([0,1])
for i in range(20):
    fib = np.append(fib, fib[-2]+fib[-1])

print(fib)

fib = np.array([0,1])
while fib[-1]< 1000000:
    fib = np.append(fib, fib[-2]+fib[-1])

print(fib)
    