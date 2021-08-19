# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:00:28 2020

@author: HP ELITEBOOK 820 G4
"""

def trapezoidal(f,a,b,n):
    h = (b-a)/n
    x = linspace(a,b,n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s
