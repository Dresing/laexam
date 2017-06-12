# coding=utf-8

import numpy as np
import sympy as sy

#--------------------------- Change of abitrary basis ----------------------------------#
#Basis 1 
S = np.array([[1,0],[0,1]])

#Basis 2 
B = np.array([[3,1],[4,1]])

# Compute transition matrix B->S by concartíng bases and calculate rref. Take the matrix after the indentity matrix. Page 212
sy.Matrix(np.concatenate((S,B), axis=1)).rref()

#Taken from the print, the transition matrix is.
B_S = np.array([[3,1],[4,1]])

#Transition matrix S->B is then given as the inverse: 1/(ad-bc) * [[d, -b], [-c, a]].
S_B = (1/np.linalg.det(B_S) * np.array([[1,-1],[-4,3]]))

#A vector "w" in basis S
w_S = np.array([[3],[-5]])

#Change the basis P_[S->B] * [w]_S 
w_B = np.dot(S_B, w_S)


#--------------------------- Change to standard basis and then to another ----------------------------------#

#Basis 1
B = np.array([[1,-1],[2,1]])

S = np.array([[3,5],[1,2]])

#Given a vector in that basis
w_B = np.array([[4],[-1]])

#Calcutelate the vector in the standard basis.
w = np.dot(B, w_B)

#Transform stanard basis vector into new basis
w_S = np.dot(np.linalg.inv(S), w)



