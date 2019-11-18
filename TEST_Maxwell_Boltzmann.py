# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:25:16 2018
@author: sfg17 28 Nov 2018

Produces plot of experimental and theoretical Maxwell Boltzmann distribution
Starting default values are enough to see the starting of the distribution,
for clearer spreads, increase Number_of_Balls and N_Collisions. 
"""

from Simulation import Simulation
from config import * 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from scipy.stats import norm

import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

#---------Parameters----------
Number_of_Balls = 100#For P-N plot
N_Collisions = 20
Container_Radius = 10

#---------Loads Simulation----------
sim = Simulation(Number_of_Balls)
sim.run(N_Collisions,animate = False)
sim.Velocities_Hist()
#print("Starts",len(sim.Velocities_Hist()))
#print(sim.Velocities_Hist())


#---------Magnitude of Positions----------
plt.figure(figsize = (8,5))
plt.title("Magnitudes of Positions to Center") 
plt.xlabel("Distances to center /m")
plt.ylabel("Frequency")
plt.hist(sim.mag_position_to_center, bins=10)
plt.savefig("FIG_mag_to_center")


#---------Distances between Two Balls, For all balls----------
plt.figure(figsize = (8,5))
plt.title("Distances Between Two Balls, for all Balls")
plt.xlabel("Distances between two balls /m")
plt.ylabel("Frequency")
plt.hist(sim.Two_Ball_Distance(),bins = 10)
plt.savefig("FIG_mag_2_balls")



#---------Histogram of all velocities to produce PDF------------
data = sim.Velocities_Hist()
(mu,sigma) = norm.fit(data)

plt.figure(figsize = (8,5))
plt.title("Simulated Maxwell Boltzmann Distribution")
plt.xlabel("Velocity /$ms^-1$")
plt.ylabel("Density")
n, bins, patches = plt.hist(data,bins = 50,normed = True)

y = mlab.normpdf(bins,mu,sigma)
l = plt.plot(bins,y,label = 'Experimental')
print("\nuncertainty",sigma,"variance",sigma*sigma,"mean",mu)

#---------Theoretical Maxwell Boltzmann Curve----------
def Maxwell_Boltzmann(x): #2D
#    print(sim.Temperature())
    A = (ball_mass/(kb * sim.Temperature()))
    exponent = (-x*x *ball_mass)/(2 * kb * sim.Temperature())
    y = A * (x) * np.exp(exponent)
    return y

x_value = bins
y_value = Maxwell_Boltzmann(x_value)

plt.plot(x_value,y_value,'r--',linewidth = 2,label = 'Theoretical')
plt.savefig("FIG_Maxwell_Boltzmann")
plt.legend()
plt.show()

print("Real Temperature:",sim.Temperature())
print("Real Pressure:",sim.Pressure(),"\nIdeal Pressure:",sim.Pressure_Ideal(),
      "\n as Particle Size decreases, Real Pressure tend to Ideal Pressure")






