
# Import of packages:
import matplotlib.pyplot as plt
import numpy as np

# Model parameters:
Kh = 3.5 # [C/V]    #Heater gain
theta_t = 23 #[s]   #Time-constant
theta_d = 3 #[s]  #Time delay
T_env = 20 #[C]     #Environmental (room) temperature

# Simulation time settings:
Ts = 0.05 # [s]                         #Time step 
t_start = 0 # [s]                       #Start time
t_stop = 300 # [s]                      #Stop time
N_sim = int((t_stop - t_start)/Ts) + 1  # Number of time-steps

# Preallocation of arrays for plotting:
t_array = np.linspace(t_start, t_stop, N_sim)   # Array for time
k_array = np.arange(0, N_sim)                   #Array for simulation loop
T_array = np.zeros(N_sim)                       #Array for output value
u_in_array = np.zeros(N_sim)                    #Array for input value
u_delay_array = np.zeros(N_sim)                 #Array for delay value

# Params of input signals:
t0 = 20 # [s]                                   #Time for first alteration 
t1 = 150  # [s]                                 #Time for second alteration 

u_in_0 = 0.0 # [V]                              #Input value
u_in_1 = 5.0 # [V]                              #Input value
u_in_2 = 1.1 # [V]                              #Input value


# Initialization:
T_init = T_env # [C]
T_k = T_init   # [C]         #Over writing room temperature as initial value

# Preallocation of array for time-delay:
Nd = int(round(theta_d/Ts)) + 1     #Calculating timedelay in slice
delay_array = np.zeros(Nd) + u_in_0 #declare the array and put u_in_0 as initial value


# Simulation loop:
for k in k_array:
    t_k = t_array[k]

    # Selecting inputs:
    if (t_k >= t_start and t_k < t0):   #Varing the input wrt. declaration above
        u_k = u_in_0
    if (t_k >= t0 and t_k < t1):
        u_k = u_in_1
    if (t_k >= t1 and t_k <= t_stop):
        u_k = u_in_2

    # Time delay:
    u_delay_k = delay_array[-1] #Choosing the last element in delay array
    delay_array_sliced = delay_array[:-1] #deleting the last element in delay_array
    delay_array = np.insert(delay_array_sliced, 0, u_k) #Inserting the u_k value at position '0' in delay_array

    # Time-derivative:
    dT_dt_k = (1/theta_t)*(T_env - T_k) + (Kh/theta_t)*u_delay_k
    
    # State update using the Euler method (``kp1'' means ``k+1''):
    T_kp1 = T_k + dT_dt_k*Ts
    
    # Arrays for plotting:
    T_array[k] = T_k                #Output signal
    u_in_array[k] = u_k             #Inputsignal
    u_delay_array[k] = u_delay_k    #Delay signal
    
    # Time shift (``kp1'' means ``k+1''):
    T_k = T_kp1


# Plotting:
plt.close('all') # Closes all figures before plotting

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
plt.legend(labels=('Temperature[$^\circ$C]', ), # Note: Comma and space!
           loc='upper right', handlelength=2, fontsize=12)

plt.subplot(2, 1, 2)
plt.grid(which='both', color='grey')
plt.ylim(0, 5.1)
plt.xlabel('t [s]')
plt.ylabel('Voltage [V]')
plt.plot(t_array, u_in_array, 'r', t_array, u_delay_array,'g')
plt.legend(labels=('Control delay signal [V]','Control signal [V]'),
           loc='upper right', handlelength=2, fontsize=12)

plt.show()
plt.savefig('Plot_sim_airheater.pdf') # pdf file of plot
airheater.txt
Displaying airheater.txt.