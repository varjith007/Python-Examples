import matplotlib.pyplot as plt
import numpy as np

#model inputs
Kh = 3.5
theta_t = 23
theta_d = 3
T_env = 20

# Simulation time settings:
Tspace = 0.05
t_start = 0
t_stop = 500 
n_sim = int((t_stop - t_start)/Tspace) + 1 

# Preallocation of arrays for plotting:
t_array = np.linspace(t_start, t_stop, n_sim) 
k_array = np.arange(0, n_sim)                  
T_array = np.zeros(n_sim)                      
u_in_array = np.zeros(n_sim)                   
u_delay_array = np.zeros(n_sim)                

# Params of input signals:
t0 = 50 # [s]                                  #1st alteration
t1 = 250  # [s]                                 #2nd alteration

u_1st = 0.0 # [V]                              #1stInput value
u_2nd = 5.0 # [V]                              #2ndInput value
u_3rd = 2.1 # [V]                              #3rdInput value


# Initialization:
T_init = T_env 
T_k = T_init          

# Preallocation of array for time-delay:
Nd = int(round(theta_d/Tspace)) + 1     
delay_array = np.zeros(Nd) + u_1st 


# Simulation loop:
for k in k_array:
    t_k = t_array[k]

    # Selecting inputs:
    if (t_k >= t_start and t_k < t0):   
        u_k = u_1st
    if (t_k >= t0 and t_k < t1):
        u_k = u_2nd
    if (t_k >= t1 and t_k <= t_stop):
        u_k = u_3rd

    # Time delay:
    u_delay_k = delay_array[-1] 
    delay_array_sliced = delay_array[:-1] 
    delay_array = np.insert(delay_array_sliced, 0, u_k) 

    # Time-derivative:
    dT_dt_k = (1/theta_t)*(T_env - T_k) + (Kh/theta_t)*u_delay_k #u_delay = (t - theta_t)
    
    # State update using the Euler method (``kplus1'' means ``k+1''):
    T_kplus1 = T_k + dT_dt_k*Tspace
    
    # Arrays for plotting:
    T_array[k] = T_k                #Output signal
    u_in_array[k] = u_k             #Inputsignal
    u_delay_array[k] = u_delay_k    #Delay signal
    
    # Time shift (``kplus1'' means ``k+1''):
    T_k = T_kplus1


# Plotting:
plt.close('all') 

fig_width_inch = 24/2.54
fig_height_inch = 18/2.54
plt.figure(num='Simulation of Air heater',
           figsize=(fig_width_inch, fig_height_inch))
plt.suptitle('Simulation of Air heater')

plt.subplot(2, 1, 1)
plt.grid(which='both', color='grey')
plt.ylim(19, 40)
plt.xlabel('t [s]')
plt.ylabel('Temperature[$^\circ$C]')
plt.plot(t_array, T_array, 'b')
plt.legend(labels=('Temperature[$^\circ$C]', ), 
           loc='upper right', handlelength=2, fontsize=12)

plt.subplot(2, 1, 2)
plt.grid(which='both', color='grey')
plt.ylim(0, 5.1)
plt.xlabel('t[s]')
plt.ylabel('Voltage[V]')
plt.plot(t_array, u_in_array, 'r', t_array, u_delay_array,'g')
plt.legend(labels=('Control delay signal[V]','Control signal[V]'),
           loc='upper right', handlelength=2, fontsize=12)

plt.show()
plt.savefig('airheater.pdf') 