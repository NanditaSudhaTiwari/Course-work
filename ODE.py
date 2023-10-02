import numpy as np
import matplotlib.pyplot as plt

def f(Num_atoms):
    return -0.1*Num_atoms
a = 0                  # start time
b = 10                 # end time
num_steps = 5         # number of time steps
h = (b-a) / num_steps  # time step size
Num_atoms = 1000       # initial condition
time_list = np.arange(a,b,h)

# create an empty list to hold the calculated N values
Num_atoms_list = []
for time in time_list:
    Num_atoms_list.append(Num_atoms)
    k1 = h*f(Num_atoms)
    k2 = h*f(Num_atoms+0.5*k1)
    k3 = h*f(Num_atoms+0.5*k2)
    k4 = h*f(Num_atoms+k3)
    Num_atoms += k4
    
def analytic_solution(time):
        return 1000*np.exp(-0.1*time)
num_steps_analytic = 1000
h_analytic = (b-a) / num_steps_analytic
time_analytic_list = np.arange(a,b,h_analytic)
Num_atoms_analytic_list = []
for time in time_analytic_list:
    Num_atoms_analytic_list.append(analytic_solution(time))
    Num_atoms = 1000
    
Num_atoms_euler_list = []
for time in time_list:
    Num_atoms_euler_list.append(Num_atoms)
    Num_atoms += h*f(Num_atoms)
    
plt.plot(time_analytic_list,Num_atoms_analytic_list,label="analytic")
plt.scatter(time_list, Num_atoms_list,label="Runge-Kutta (fourth-order)")
plt.scatter(time_list, Num_atoms_euler_list,label="Euler's method")
plt.xlabel("time")
plt.ylabel("Number of atoms")
plt.legend()
plt.show()






