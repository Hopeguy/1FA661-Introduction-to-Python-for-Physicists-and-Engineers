# Assignment 1 Joakim Ginste
import numpy

# Question 1

pulses = numpy.loadtxt("pulses.csv", delimiter=',')
print(pulses)

for pulse in pulses:
    Voltages = pulse[1:]/(2**10 - 1) * 0.6