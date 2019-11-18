# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:27:30 2018

@author: sfg17 28 Nov 2018
"""

from Ball import Ball
from config import *
import pylab as pl
import numpy as np

class Container(Ball):
    """
    Container Class
    
    Defines characteristics of the container. Derived from Ball as is 
    essentially a larger ball
    
    Parameters
    ----------
    _container_collide - performs a collision between a ball and a container
    
    _get_patch - creates a container patch that is used to represent the 
    container in an animation. 
    """
    def __init__(self,radius = None,position = [0,0],velocity = [0,0]):
        self.radius = con_radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        
    
    def _container_collide(self,other):
        """
        Calculates the new velocity of the ball after a collision with the
        container
        """
        # 1 - Ball
        # 2 - Container
        u_ball = other._vel()
        r = np.subtract(self.position,other.position)
        r_normal = r/np.linalg.norm(r)

        u_radial = np.dot(u_ball,r_normal)*r_normal
        u_tangent = - u_radial + u_ball

        v = - u_radial + u_tangent
        
        return v
        
    def _get_patch(self):
        """
        Returns patch of container for animation
        """
        patch = pl.Circle(self.position, 10, ec='b', fill=False, ls='solid')
        return patch
    
    