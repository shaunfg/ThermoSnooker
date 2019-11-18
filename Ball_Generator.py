# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:28:12 2018

@author: sfg17 28 Nov 2018
"""

from Ball import Ball
from config import *
import numpy as np

class Ball_Generator(Ball):
    """
    Generates Balls to be used in simulating collisions
    
    Parameters
    ----------
    _balls: Returns a list of balls with randomly generated positions and 
    velocities with mass and radii defined in the config.py file. 
    
    _vel_init: Returns a list of initial velocities, useful in histogram
    plots
    """
    
    def __init__(self, mass = None, radius = Max_Radius, position =[0,0], 
                 velocity =[0,0],con_rad= con_radius):

        self.ball_list = []
        self.radius = radius
        self.mass = ball_mass
        self.vel_initial = []
        self.con_radius = con_rad
        

            

    def __ball_overlap(self,pos_check,radius):
        """
        Returns a True / False statement that is used in the While loop,
        that excludes randomized ball positions that overlap with other balls.
        """
        ball_overlap = False
        
        for i in range(len(self.ball_list)):
            r_dash = pos_check - self.ball_list[i]._pos()
            R = radius + self.ball_list[i]._rad()
            if np.linalg.norm(r_dash) <= R:
                ball_overlap = True
        
        return ball_overlap
                
    def __outside_container(self,pos,ball_radius):
        """
        Returns a True / False statement that is used in the While loop,
        that excludes balls that spawn outside the container.
        """
        outside_container = False
        
        if np.dot(pos,pos) > (ball_radius - self.con_radius)**2:
            outside_container = True
        
        return outside_container
    
    def _balls(self,Number_of_Balls):
        """
        Returns the list of randomly generated balls
        """
        
        print("Generating Balls...")

        con_range = (-self.con_radius,self.con_radius,2)
        vel_range = (-Max_vel,Max_vel,2)
        
        for i in range(Number_of_Balls):
            rand_pos = np.random.uniform(*con_range)
            rand_vel = np.random.uniform(*vel_range)
            
            while (self.__outside_container(rand_pos,self.radius) or 
                   self.__ball_overlap(rand_pos,self.radius)):
                rand_pos = np.random.uniform(*con_range)
                        
            rand_ball = Ball(self.mass,self.radius,rand_pos,rand_vel)
            self.ball_list.append(rand_ball)
            
            self.vel_initial.append(rand_vel)
            
            print("Ball",[i+1])
        return self.ball_list
    
    def _vel_init(self):
        """
        Returns a list of the initial starting values of generated velocities
        Used in Histogram plots
        """
        vel = []
        for i in range(len(self.vel_initial)):
            vel.append(np.linalg.norm(self.vel_initial[i]))
            
        return vel
    