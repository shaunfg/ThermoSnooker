—————————————————————————————————————————————————
| 2D Elastic Collisions In a Circular Container |
—————————————————————————————————————————————————
 
CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * How to run
 * Configuration
 * Troubleshooting & FAQ
 
INTRODUCTION
------------
A simulation was created using python to simulate the elastic collision of circular particles in a circular container, to investigate the laws of thermodynamics. This simulation can demonstrate the thermodynamic relations between pressure, volume, temperature and number of particles. Along with investigating the Maxwell Boltzmann distribution and constants for Van Der Waal's gas equation.
 
REQUIREMENTS
------------
Spyder 3.0 or above. 
 
Packaages include: 
	* Numpy
	* Pylab
	* Matplotlib
 
 
HOW TO RUN
------------
No installation needed. Just open the file and click run. 
 
TEST_(x) files represent test scripts to extract simulation data from the program. These include
	* TEST_Animation.py 
		(To test animation)
	* TEST_Thermodynamics.py 
		(To test thermodynamic relations)
	* TEST_Maxwell_Boltzmann.py 
		(To test Maxwell-Boltzmann Distribtion) 
	* TEST_VDW.py 
		(To test Van Der Waal’s Gases)
 
Classes include 
	* Ball.py
	* Container.py
	* Ball_Generator.py
	* Simualtion.py
 
Config Files include:
	* config.py
 
NOTE: DO NOT CHANGE NAMES OF FILES. 
 
CONFIGURATION
------------
Found inside the config files are the default parameters for the simulation. Parameters by default are set to an O2 oxygen gas at room temperature and pressure conditions.  Key parameters can also be changed within any TEST_(x) file, thus might not be necessary to configure parameters using this file. Only open if parameter not listed at the top of a TEST_(x) file. 
 
TROUBLESHOOTING & FAQ
------------
Please contact @sfg17 for issues, details and questions. 
