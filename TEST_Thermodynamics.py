#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:25:16 2018
@author: sfg17 28 Nov 2018

Runs Simulation for Elastic Collisions, producing the thermodynamic relations
    1. P proportionl to N
    2. P proportional to 1/V
    3. P proportional to T
where P is pressure, N is number of balls/particles, V is volume and T is
temperature

Checks for energy and momentum conservations are found at the 
bottom of this script.

If other parameters would like to be changed, please change accordingly on
config.py
"""

from Simulation import Simulation
from config import *
import matplotlib.pyplot as plt
import numpy as np

# Thermodynamic Graphs

#----------Parameters-------------
Number_of_Balls = 10#For P-N plot
N_Collisions = 10
N_Plots = 10 #For P-T plot and P-V plot
Container_Radius = 10

#----------P against N-------------
n_i = np.linspace(1,Number_of_Balls,Number_of_Balls)
pressure = []
pressure_error = []
for i in range (1,Number_of_Balls+1):
    s = Simulation(i)
    s.run(N_Collisions)
    pressure.append(s.Pressure())
    pressure_error.append(s.std_dev())

plt.figure(figsize = (8,5))
plt.title("Pressure against Number of Balls")
plt.xlabel("Number of Balls")
plt.ylabel("Pressure/ Pa")
plt.plot(n_i,pressure,'x',color = 'C1')
plt.plot(np.unique(n_i), np.poly1d(np.polyfit(n_i,pressure, 1))(
        np.unique(n_i)),color = 'C0')
plt.errorbar(n_i,pressure,yerr = pressure_error,fmt='x',mew=1,ms=0,
             color = 'gray')
plt.savefig("FIG_P_against_N")
  
#----------P against V-------------
volume = []
pressure_2 = []
pressure_error_2 = []
radii = []

for i in np.linspace(0,Container_Radius,N_Plots):
    s = Simulation(Number_of_Balls,i)
    s.run(N_Collisions)
    volume.append(s.Volume())
    pressure_2.append(s.Pressure())
    radii.append(i)
    pressure_error_2.append(s.std_dev())

plt.figure(figsize = (8,5))
plt.title("Pressure against Volume")  
plt.plot(volume,pressure_2,'x',color = 'C0')
plt.errorbar(volume,pressure_2,yerr = pressure_error_2,fmt='x',mew=1,
             ms=0,color = 'gray')
plt.xlabel("1/Volume / $m^3$")
plt.ylabel("Pressure / Pa")
plt.savefig("FIG_P_against_V")

#----------P against T-------------
temperature = []
pressure_3 = []
pressure_ideal = []
pressure_error_3 = []

for i in np.linspace(1,Container_Radius,N_Plots):
    s = Simulation(Number_of_Balls)
    s.run(N_Collisions)
    temperature.append(s.Temperature())
    pressure_3.append(s.Pressure())    
    pressure_ideal.append(s.Pressure_Ideal())
    pressure_error_3.append(s.std_dev())
    
plt.figure(figsize = (8,5))
plt.title("Pressure against Temperature")
plt.xlabel("Temperature /K")
plt.ylabel("Pressure /Pa")
plt.plot(temperature,pressure_3,'x',color = 'C1')
plt.errorbar(temperature,pressure_3,yerr = pressure_error_3,fmt='x',
             mew=1,ms=0, color ='gray')
line_real = plt.plot(np.unique(temperature), np.poly1d(np.polyfit(temperature,
                     pressure_3,1))(np.unique(temperature)),color = 'C0',
                    label = 'Real Pressure')
line_pressure = plt.plot(np.unique(temperature), np.poly1d(np.polyfit(
        temperature,pressure_ideal, 1))(np.unique(temperature)),color = 'C3', 
        label = 'Ideal Pressure')

plt.legend()

plt.savefig("FIG_P_against_T")

#----------E and p Conservation-------------
sim = Simulation(1,)
sim.run(N_collisions,animate = False) #Set (animate = True) to see animation

print("\nReal Temperature:",sim.Temperature(),"K")
print("Real Pressure:",sim.Pressure(),"Pa","\nIdeal Pressure:",
      sim.Pressure_Ideal(),"Pa",
      "\n as Particle Size decreases, Real Pressure tend to Ideal Pressure")

sim.KE_Conservation()
sim.P_Conservation()

#----------Graph Data-------------
print("P on N points:",len(pressure))
print("P on V points:",len(pressure_2))
print("P on T points:",len(pressure_3))

    