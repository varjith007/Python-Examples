import numpy as np
import matplotlib.pyplot as plt 
import math


def xy(v0, t):
    g = 9.8
    y = v0*t - 0.5*g*t**2
    return y

    
t = np.linspace(0,1,1000)
l = len(t-1)
ans = np.zeros(l)

for i in range(0,l,1):
    ans[i] = xy(5,t[i])
    

largest_height = ans[0]

for i in range(len(ans)):
    if ans[i] > largest_height:
        largest_height = ans[i]
        
print('the heighest point the ball travelled is = {:f}'.format(largest_height))
plt.plot(t,ans)
plt.xlabel('time')
plt.ylabel('Height of ball')
plt.legend('Distance travelled by the ball')
plt.show()


    