# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:29:01 2018

@author: sfg17 28 Nov 2018
"""

import numpy as np
import pylab as pl

from config import *
from Container import Container
from Ball import Ball
from Ball_Generator import Ball_Generator

np.seterr(divide='ignore', invalid='ignore')

class Simulation:
    """
    Simulation Class
    
    Checks if next collision is container or ball collision and 
    collides all the balls .
    
    Parameters
    ----------
    run - runs code
    
    KE_Conservation - Checks if Kinetic Energy is conserved, returns True/False
    
    p_Conservation - Checks if momentum is conserved, returns True/False
    
    Two_Ball_Distance - Returns Distances between two balls for all cases,
        useful in histogram plotting
    
    Temperature - Returns temperature of system
    
    Pressure - Returns real temperature of system, with real mass and volume
    
    Pressure_Ideal - Returns pressure according to ideal gas law

    Velocities_Hist - Returns velocities of before and after all collisions,
        useful in Histogram plotting. 
    """
    def __init__(self,Number_of_Balls, con_rad = con_radius):
        self.container = Container()
        generate_balls = Ball_Generator()
        self.ball_list = generate_balls._balls(Number_of_Balls)
        
        self.mag_position_to_center = []
        self.position_to_center = []
        
        self.KE_CONS = ()
        self.P_CONS  = ()
        
        self.p_change = []
        self.total_time = 0.0
        self.KE_Total = ()
        
        self.velocity_hist = [generate_balls._vel_init()]
        
        self.N_Balls = len(self.ball_list)
        
        self.con_radius = con_rad

        
    
    def _next_collision(self):
                
        N_Balls = len(self.ball_list)
        
        time_list_b = []
        var_list_ball= [] #Index Number of collision. 
    
        for i in range(N_Balls):
            a = self.ball_list[i]
            
            for j in range(i+1,N_Balls):
                b = self.ball_list[j]
                time = a._time_to_collision(b)
                time_list_b.append(time)
                var_list_ball.append([i,j])
        
        time_min_ball = ()
        
        if len([x for x in time_list_b if x!=0]) == 0:
            time_min_ball = 0
        elif all(i < 0 for i in [x for x in time_list_b if x!=0]) ==True:
            time_min_ball = 0
        else:
            time_min_ball = min([x for x in time_list_b if x>0])

        time_container= []
        var_list_container = []
        for j in range(N_Balls):
            time = self.container._time_to_collision(self.ball_list[j], 
                                                     container = True)
            time_container.append(time)
            var_list_container.append([j])

        time_min_container = min([x for x in time_container if str(x) != 
                                  'None'])
        
        #Conservation Tests
        def KE(m,v):
            KE = 1/2 * m * v * v
            return KE
       
        def p(m,v):
            p = m * v
            return p
        
        def p_del(m,v1,v2):
            del_p = m*(v1-v2)
            mag_del_p = np.linalg.norm(del_p)
            return mag_del_p

        def CONS_Check(KE_Before,KE_After,p_Before,p_After):
            if int(np.sum(KE_Before)) == int(np.sum(KE_After)):
                self.KE_CONS = True
                self.KE_Total = np.sum(KE_After)
            else:
                self.KE_CONS = False
            if int(np.sum(p_Before)) == int(np.sum(p_After)):
                self.P_CONS = True
                self.KE_Total = np.sum(KE_After)
            else:
                self.P_CONS = False

        #Ball - Ball Collision
        if time_min_ball < time_min_container and float(time_min_ball) != 0:

            tmin = time_min_ball
            t_i = time_list_b.index(tmin) # finds the index value of tmin
            v_i_min = var_list_ball[t_i]
            
            for i in range(N_Balls):
                newpos = self.ball_list[i]._move(tmin)
                self.position_to_center.append(newpos)
                self.mag_position_to_center.append(np.linalg.norm(newpos))

            Ball_1 = self.ball_list[v_i_min[0]]
            Ball_2 = self.ball_list[v_i_min[1]]
            
            KE_Before = []
            KE_After  = []
            p_After = []
            p_Before = []            

            for i in range(N_Balls):
                energies = KE(ball_mass,self.ball_list[i]._vel())
                KE_Before.append(energies)
                
                momentums = p(ball_mass,self.ball_list[i]._vel())
                p_Before.append(momentums)

            collision = Ball_1._collide(Ball_2)
            Ball_1.velocity = collision[0]
            Ball_2.velocity = collision[1]
            
            for i in range(N_Balls):
                energies = KE(ball_mass,self.ball_list[i]._vel())
                KE_After.append(energies)
                
                momentums = p(ball_mass,self.ball_list[i]._vel())
                p_After.append(momentums)
                
            self.total_time += tmin
            
            CONS_Check(KE_Before,KE_After,p_Before,p_After)
        
        #Ball - Container Collision
        else:
            
            tmin = time_min_container
            t_i = time_container.index(tmin) # finds the index value of tmin
            v_i_min = var_list_container[t_i]
            for i in range(N_Balls):
                newpos = self.ball_list[i]._move(tmin) 
                self.position_to_center.append(newpos)
                self.mag_position_to_center.append(np.linalg.norm(newpos))

            Ball_1 = self.ball_list[v_i_min[0]]

            KE_Before = []
            KE_After  = []
            p_After = []
            p_Before = [] 
            
            for i in range(N_Balls):
                energies = KE(ball_mass,self.ball_list[i]._vel())
                KE_Before.append(energies)
                
                momentums = p(ball_mass,self.ball_list[i]._vel())
                p_Before.append(momentums)                
                
            v_before = Ball_1.velocity
            v_after = self.container._container_collide(Ball_1)
            Ball_1.velocity = v_after
                
            for i in range(N_Balls):
                energies = KE(ball_mass,self.ball_list[i]._vel())
                KE_After.append(energies)
                
                momentums = p(ball_mass,self.ball_list[i]._vel())
                p_After.append(momentums)
                
            self.p_change.append(p_del(ball_mass,v_before,v_after))
                
            self.total_time += tmin

            CONS_Check(KE_Before,KE_After,p_Before,p_After)
        return
                
    def run(self, N_collisions, animate=False):
        if animate:
            f = pl.figure()
            ax = pl.axes(xlim=(-10, 10), ylim=(-10, 10))
            ax.add_artist(self.container._get_patch())
            for ball in self.ball_list:   
                ax.add_patch(ball._get_patch())
        for frame in range(N_collisions):
            print("Collision Number:",frame)
            self._next_collision()
            if animate:
                pl.pause(0.1)
        if animate:
            pl.show()

    def KE_Conservation(self):
        """
        Returns if Kinetic Energy is Conserved or not. (True/False)
        """
        return print("KE Conservation:", self.KE_CONS)
    
    def P_Conservation(self):
        return print("P Conservation:",self.P_CONS)
        
    def Two_Ball_Distance(self):
        distances = []
        for i in range(len(self.ball_list)):
            pos_1 = self.position_to_center[i]
            for j in range(i+1,len(self.ball_list)):
                pos_2 = self.position_to_center[j]
                dis = np.linalg.norm(np.subtract(pos_1,pos_2))
                distances.append(dis)
        return distances

    def Temperature(self):
        T = self.KE_Total/ (self.N_Balls * kb)
        return T
    
    def Pressure(self): #By Change of Momentum
        P = np.sum(self.p_change)/(self.total_time* 2 * np.pi * 
                  self.con_radius)
        return P
    
    def Pressure_Ideal(self): #By Ideal Gas
        V = np.pi * self.con_radius * self.con_radius
        P_ideal = self.N_Balls * kb * self.Temperature() / (V)
        return P_ideal
    
    def Velocities_Hist(self):
        return self.velocity_hist
    
    def Volume(self):
        V = np.pi * self.con_radius * self.con_radius
        return V
    
    def std_dev(self):
        s = np.std(self.p_change)
        s = s/(self.total_time* 2 * np.pi * self.con_radius)
        return s
    
    def Ball_Volume(self):
        V = []
        for i in range(len(self.ball_list)):
            V.append(2* np.pi * self.ball_list[i]._rad())
        return np.sum(V)
            
    
