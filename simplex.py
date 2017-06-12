# coding=utf-8
from util import latex
from fractions import Fraction as f
import sympy as sy
import numpy as np
from sympy import Rational as R
from gurobipy import *
from math import * 
from operator import itemgetter


A = np.array([
	[R('-20'), R('-35'), R('-95'), R('1'), R('0'), R('-319')],
	[R('-5'), R('-9'), R('-23'), R('0'), R('1'), R('0')],

	])
A.astype('object')



class Simplex:

	def __init__(self, A):
		self.A = A
		self.height = len(A)
		self.width = len(A[0])
		self.c = A[self.height-1]


	def primalPivot(self, i = 0, doPrint=True):
		if self.c[i] <= 0:
			print "Error, cannot iterate on negative or zero c at idx: " + str(i)
			print self.c
			exit(0)

		if doPrint: print 'We need to choose the pivot based the smallest value of $\\frac{b_i}{a_i'+str(i)+'}$ where $i$ is a given row.\\\\'
		smallest = float("inf")
		index = -1
		if doPrint: print "$min\\{"
		for idx,row in enumerate(self.A):
			if row[i] <= 0 or idx == self.height-1:
				continue
			cur = row[self.width-1]/row[i]

			if doPrint: print str(cur) + ","

			if(cur < smallest):
				smallest = cur
				index = idx

		if index < 0:
			print "Error in simplex. Could find a pivot in the column."
			exit(1)
		
		if doPrint: print "\\} = "+str(smallest)+"$\\\\\\ \nThus, we can deduce the pivot to be at $a_"+ str(index) + str(i) + "$\\\\\\\\"

		return (index, smallest)
	def iteration(self, pivot, dual=False, doPrint=True):
		if not dual:
			column = pivot
			row, val = self.primalPivot(column, doPrint)
		else:
			row = pivot
			column, val = self.dualPivot(row, doPrint)
		if doPrint: print "Putting variable from column " + str(column) + " in basis: \\\\"
		divider = self.A[row][column]
		if doPrint: print "R" + str(row) + "'  = R" + str(row) + "/(" + str(divider)+") \\\\" 
		pivotRow = map(lambda x: x/divider,self.A[row])
		self.A[row] = pivotRow


		for idx,r in enumerate(self.A):
			if idx == row:
				continue
			if doPrint: print "R" + str(idx) + "' = R" + str(idx) + " + (" + str(-A[idx][column]) + ") * R" + str(row) + "' \\\\"
			self.A[idx]= self.A[idx] + map(lambda x: -A[idx][column] *x, pivotRow)


	def dualPivot(self, row, doPrint):

		if 0 < A[row][self.width-1]:
			print "Cannot perform dual."
			exit(0)

		if doPrint: print 'We need to choose the pivot based the smallest value of $\\frac{c_j}{a_'+str(row)+'j}$ where $j$ is a given column.\\\\'

		smallest = float("inf")
		index = -1
		if doPrint: print "$min\\{"
		for idx,p in enumerate(self.A[row]):
			if idx == self.width - 1:
				continue
			if p < 0:
				cur =  ((self.A[self.height-1][idx])/p)
				if doPrint: print str(cur) + ","
				if cur < smallest:
					smallest = cur
					index = idx

		if index < 0:
			print "Cannot perform dual. (2)"
			exit(0)

		if doPrint: print "\\} = "+str(smallest)+"$\\\\\\ \nThus, we can deduce the pivot to be at $a_"+ str(row) + "," + str(index) + "$\\\\\\\\"

		return (index, smallest)




		


	def isFraction(self, n):
		return not float(n).is_integer()






S = Simplex(A)

S.iteration(0, dual=True, doPrint=True)
#S.iteration(row=1, dual=True ,doPrint=False)
#S.iteration(column=4,doPrint=False)

print latex(S.A)



