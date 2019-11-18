#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:40:59 2018
@author: sfg17 28 Nov 2018

Runs VDW gas calculations and calculates correction terms of 'a' and 'b' seen 
in VDWequation for real gases. 
"""

from Simulation import Simulation
from config import *
import numpy as np


#--------Paramenters----------
N_collisions = 10
repeats = 10
Number_of_Balls = 100

#--------VDW: a,b-----------
a = []
b = []
P = []

for i in range(repeats):
    sim = Simulation(Number_of_Balls)
    sim.run(N_collisions)
    V = sim.Ball_Volume()
    Nb = Number_of_Balls * V #2d ball
    constants = (Number_of_Balls * kb * sim.Temperature())/(2 * np.pi * 
                con_radius - Nb)

    a.append((V*V/Number_of_Balls**2)*(constants - sim.Pressure()))
    b.append(2*np.pi* Max_Radius)
    P.append(sim.Pressure())

print("\nNumber of Repeats = ",repeats)
print("\nPressure =",np.mean(P),"+/-",np.std(P),"Pa")
print("Volume of Balls =",V,"m^3")
print("a = ",np.mean(a), "+/-",np.std(a))
print("b = ", np.mean(b), "+/-",np.std(b))

