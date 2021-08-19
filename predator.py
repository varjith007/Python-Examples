# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:46:58 2020

@author: HP ELITEBOOK 820 G4
"""

import numpy as np
import matplotlib.pyplot as plt

def dxdt(x,y):
    return x*(alpha - beta*y)

def dydt(x,y):
    return -y*(delta - epsilon*x)

alpha = 1.8
beta = 0.8
delta = 1.2
epsilon = 1.2
a = 0.0
b = 10.0
dt = 0.001
0
#x= np.zeros(10001)
#y = np.zeros(10001)

x[0] = 2.0
y[0] = 2.0
time = np.linspace(a, b, b*1000 + 1)

for i in range(0,len(x)-1,1):
    x[i + 1] = x[i] + dt*dxdt(x[i],y[i])
    y[i + 1] = y[i] + dt*dydt(x[i],y[i])
    

plt.plot(time,x,'b',time,y,'r')
plt.legend('rabbit','fox')
plt.xlabel('time')
plt.ylabel('predator numvers')

