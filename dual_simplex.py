#1. Find a row with a negative b value

#2. Find the column where the relation between c_j/A_j is the smallest, the pivot has to be negative.

#Put the pivot in basis. If all in b are positive are positive, go back to simplex. If optimal, we can end.

#--------------- Cutting Plane - Chvátal-Gomory Algorithm ---------------#

#1. Select a row that is fractional in b from the optimal solution, if none exists, the solution is already optimal for the integer program.

#2. For all columns (j) in the row (a), calculate, this is the new constraint that can be added to the simplex.
#   (a_1 - floor(a_1)) x_1 + ... + (a_j - floor(a_j)) x_j >= b_i - floor(b_i)

#Get the simplex back to optimality, rinse and repeat.


