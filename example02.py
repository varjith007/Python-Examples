import random
import numpy as np
import math 

a = np.zeros(6)



for i in range(len(a)):
    a[i] = random.uniform(0,10)

print(a)
    



for i in range(len(a)):
    smallest = a[i]
    i_min = i
    for j in range(i+1,6,1):
        if a[j] <= smallest:
            smallest = a[j]
            i_smallest = j
    
    switch = a[i]
    a[i] = a[i_smallest]
    a[i_smallest] = switch 

    
            
        
print(a)