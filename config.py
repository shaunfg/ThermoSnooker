# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:30:12 2018
@author: sfg17

CONFIG

Change values accordingly to assess different situations in result.
NOTE: Only modify if parameter not listed at the top of TEST_(x) file. 

DEFAULT DATA: Oxygen (O2) Molecule 
"""
#Number of Balls / Particles (Default value)
Number_of_Balls = 10

#Ball Variables
Max_Radius = 0.5 #Set to see animation. For O2: 0.3E-10
ball_mass = 2* 2.6E-26
Max_vel = 1.

#Container Variables
con_radius = 10.
con_position = [0.,0.]
con_velocity = [0.,0.]

#Animation
N_collisions = 10
min_time = 1E-5 #Used to avoid float errors

#Constants
kb = 1.38E-23


