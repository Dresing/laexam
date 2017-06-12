# coding=utf-8
from util import latex
from fractions import Fraction as f
import sympy as sy
import numpy as np
from gurobipy import *
from math import * 

###DM545 2015
##1.C
#-----------------Select Constraint --------------------#

#Take the b values for those variables in basis that are not slack. Take max after.
 
#max{min{3/2 −⌊ 3/2 ⌋,1−3/2 +⌊ 3/2 ⌋},min{7/4 −⌊ 7/4 ⌋,1−7/4 +⌊ 7/4 ⌋}}=

def findVictim(b = []):
	for n in(map(lambda v: min(v - f(floor(v)), f(1) - v + f(floor(v))), b)):
		print n




findVictim([f(1,5),f(2,5)])


     	
 	
 
#max{min{3/2 −⌊ 3/2 ⌋,1−3/2 +⌊ 3/2 ⌋},min{7/4 −⌊ 7/4 ⌋,1−7/4 +⌊ 7/4 ⌋}}=
 	 	 	 	 	 	 	 	 
 	
#max{0.5,0.25}=1
 	 	 	 	 	 	 	 	 
#Hence we branch on the first variable:
#x1≤ ⌊ 3/2⌋      ∨      x1≥ ⌈ 3/2⌉    