# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:26:18 2018

@author: sfg17 28 Nov 2018
"""

import numpy as np 
from config import *
import pylab as pl


class Ball:
    """
    Ball Class 
    Defines the properties of the Ball
    
    Parameters
    ----------
    _pos - Returns position of the ball
    _vel - Returns velocity of the ball
    _move - moves ball to a new position over a time
    _rad - Returns radii of ball
    _time_to_collision - returns the time to collision between a ball and ball
    or ball and container
    _collide - performs a collision between two balls
    _get_patch - produces a ball patch that represents a ball in an animation

    """
    
    def __init__(self,mass = None,radius = Max_Radius,position = None,
                 velocity = None):
        self.mass = ball_mass
        self.radius = Max_Radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.patch = pl.Circle(self.position,self.radius , fc='r',
                               edgecolor = 'k')
        
    def _pos(self):
        """
        Returns position of the ball
        """
        return self.position
    
    def _vel(self):
        """
        Returns velocity of the ball
        """
        return self.velocity
    
    def _move(self,dt):
        """
        Calculates new position of the ball and updates the position of the 
        ball
        
        If animate = True, updates patch of ball
        """
        r_dash = np.add(self.position, self.velocity*dt)
        self.position = r_dash
        self.patch.center = r_dash
        return r_dash
    
    def _rad(self):
        """
        Returns radius of the ball
        """
        return self.radius
    
    def _time_to_collision(self,other, container = False):
        
        """
        Calculates the time to collision between two balls, or between a
        container and a ball
        """
        
        r = np.subtract(self.position,other.position)
        v = np.subtract(self.velocity,other.velocity)
        
        if container:
            R = self.radius - other.radius
        else:
            R = self.radius + other.radius     
        
        
        dt_plus = (-(2*np.dot(r,v)) + np.sqrt((2*np.dot(r,v))**2-4*np.dot(v,v)*
                    (np.dot(r,r)-R**2)))/(2*np.dot(v,v))

        dt_minus = (-(2*np.dot(r,v)) - np.sqrt((2*np.dot(r,v))**2-4*np.dot(v,v)
                    *(np.dot(r,r)-R**2)))/(2*np.dot(v,v))
            
        if dt_minus > min_time:
            return min([dt_plus,dt_minus])
        elif np.isnan(dt_plus) == True:
            return np.nan_to_num(dt_plus)
        elif abs(dt_plus) < min_time:
            return 0
        else:
            return dt_plus
    
    def _collide(self,other):
        """
        Finds the new velocity of two balls after a collision,using Momentum 
        and Energy Conservation
        """
        m1 = self.mass
        m2 = other.mass
        v1 = np.array(self.velocity)
        v2 = np.array(other.velocity)
        x1 = self.position
        x2 = other.position
        
        v1_dash = v1 - ( (2*m2) * np.dot(v1-v2,x1-x2) * (x1-x2) ) / ( 
                (m1+m2) * (x1-x2).dot(x1-x2) )
        v2_dash = v2 - ( (2*m1) * np.dot(v2-v1,x2-x1) * (x2-x1) ) / ( 
                (m1+m2) * (x1-x2).dot(x1-x2) )

        
        return [v1_dash,v2_dash]
    
    def _get_patch(self):
        """
        Returns patch of ball for animation
        """
        return self.patch

    

    
    