# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:58:57 2021

@author: Joakim
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-20,20,1001)
y = np.log(1/np.sin(x)**2)

plt.plot(x,y, label = 'sinsxx', lw = 4)
plt.legend(loc = 4)

theta = np.linspace(0, 2.*np.pi, 1000)
a = 1.
r = 2 * a * (1. + np.cos(theta))
plt.polar(theta, r)
plt.show()
