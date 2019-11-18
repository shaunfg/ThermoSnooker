#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:25:16 2018
@author: sfg17 28 Nov 2018

Runs Animation of elastic collision in a 2D circular container
"""

from Simulation import Simulation
from config import *

#---------Parameters----------
Number_of_Balls = 15 #Default is 10 if left blank
N_collisions = 100 #Default is 10 if left blank

#---------Runs Animation----------
sim = Simulation(Number_of_Balls)
sim.run(N_collisions,animate = True)