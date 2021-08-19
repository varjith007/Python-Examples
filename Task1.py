# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:08:09 2020

Industrial optimizaiton course. 

Solving LP task.


@author: ywa
"""

from scipy.optimize import linprog


c = [-45, -60, -50]
A = [[20, 10, 10],
     [12, 28, 16],
     [15, 6,  16],
     [10, 15, 0]]
b= [2400, 2400, 2400, 2400]

bnd = ([0,100], [0,60], [0,40])

res = linprog(c, A_ub = A, b_ub = b, bounds = bnd, method = 'simplex', options = {'disp': True})

# production
print('Production of P= ',round(res.x[0],2))
print('Production of Q= ',round(res.x[1],2))
print('Production of R= ',round(res.x[2],2))

# profit
Profit_max = -(res.fun +6000)
print('Max profit = ', Profit_max)

# machine time
Machine_A = sum(A[0]*res.x)
Machine_B = sum(A[1]*res.x)
Machine_C = sum(A[2]*res.x)
Machine_D = sum(A[3]*res.x)
print('Machining time of A=',round(Machine_A,0))
print('Machining time of B=',round(Machine_B,0))
print('Machining time of C=',round(Machine_C,0))
print('Machining time of D=',round(Machine_D,0))
