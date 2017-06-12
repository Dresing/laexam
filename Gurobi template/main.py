# coding=utf-8
from fractions import Fraction
#Fraction(0.25)
import sympy as sy
import numpy as np
np.set_printoptions(precision=5,suppress=True)


#Given a simplex matrix
A = np.array([
	[10,5,1,0,0], 
	[6,6,0,1,0],
	[4.5,18,0,0,1],
])

C = np.array([[-9,-7,0,0,0]]) 

#RHS
b = np.array([[50],[36],[81]]) 

#Current basis
x_b = [0,1,4]

#Not in basis
x_n = filter(lambda x: x not in x_b ,range(0, len(A[0])-1))

#Calculate coeficients
C_b = [C[0][i] for i in x_b]
C_n = [C[0][i] for i in x_n]

#Columns from the initial tablaue constructed by currently basis
A_b = np.array([[x[y] for y in x_b] for x in A])


#Columns in the initial tablaue NOT currently in basis
A_n = np.array([[x[y] for y in x_n] for x in A])

#Take the inverse of A_b
A_b_i = np.linalg.inv(A_b)

#Simplex multiplier
y = np.dot(C_b, A_b_i)

#Calculate the new A_n
A_new_n = np.dot(A_b_i, A_n)

#Calculate the new Coeficients for variables not in basis.
C_new_n = C_n - np.dot(y, A_n)

#New RHS (b)
b_new = np.dot(A_b_i, b) 
print b_new

#print c_b[0][1]#np.dot(A_b_i, A_n)