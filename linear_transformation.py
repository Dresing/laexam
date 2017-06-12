# coding=utf-8

import numpy as np
import sympy as sy

#--------------------------- Linear Transformation (Scaling) ----------------------------------#

#Basis 1 
S = np.array([[1,0],[0,1]])

#Basis 2 
B = np.array([[3,1],[4,1]])

#Transition matrixes
B_S = np.array([[3,1],[4,1]])
S_B = (1/np.linalg.det(B_S) * np.array([[1,-1],[-4,3]]))

#Transformation matrix for basis 2. Works by scaling the first vector of the basis by a factor of 0.5 (u_1 = [3,4]_T) and
#the second by a factor of 6 (u_2 = [1,1]_T)
A_b = np.array([[0.5, 0], [0,6]])

#Now for any vector [x]_b in basis B, we can apply the transformation
#-- T[x]_b = A_b * [x]_b

#To obtain the transformation matrix in basis S we can derive it as follows 
#-- T[x]_s = A_s * [x]_s

#We can derrive the transformation matrix of basis S by the following logic
#-- T[x]_s = P_b->s *T[x]_b = P_b->s * (A_b * x_b) = P_b->s * (A_b * (P_s->b * x_s)) = A_s * x_s -> A_s = P_b->s * A_b * P_s->b

#It implies that (last part of above line)
#-- A_s = P_b->s * A_b * P_s->b

A_s = np.dot(np.dot(B_S, A_b), S_B) 

#Given the transformation matrix we can calculate the transformation of an abitrary vector in basis S or B

#Example:

# Given an abitrary vector x_s in the basis of S.
x_s = np.array([[3],[-5]])

#The transformation is given as 
T_x_s = np.dot(A_s, x_s)

M = np.array([[-1,1],[1/3,1]])
T = np.array([[1,0],[0,5]])


print np.linalg.det(np.array([[-1,1],[3,-3]]))



