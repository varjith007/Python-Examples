# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:32:08 2020

@author: HP ELITEBOOK 820 G4
"""


import numpy as np 
import matplotlib.pyplot as plt

t_int = 0
t_fin = 4
n = 10;
dt = (t_fin - t_int)/n
time = linspace(t_int,t_fin,n)

cn = np.zeros(n-1)

def midpoint(f,a,b,n):
    h = (b-a)/n
    f_sum = 0
    for i in range(0,n,1):
        x = (a + h/2.0) + i*h
        f_sum = f_sum +f(x)
        return h*f_sum

def g(y):
    return y-y**2
    

for i in range(0,n-1,1):
    0.5*dt*cn[i+1]**2 - 0.5*dt*cn[i+1] + cn[i+1] = 0.5*dt*cn[i] - 0.5*dt*cn[i]**2 + cn[i]

m_sum = midpoint(g,0,4,10)

print(m_sum)

plt.plot(time,cn)
plt.xlabel('time')
plt.ylabel('function')
plt.show()
