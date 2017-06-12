from util import latex
from fractions import Fraction as f
import sympy as sy
import numpy as np
from gurobipy import *

m = Model("TSP0")
m.setParam(GRB.param.Presolve, 0)
m.setParam(GRB.param.Method, 0)
m.setParam(GRB.param.MIPGap, 1e-7)

######### BEGIN: Write here your model for Task 1



x = m.addVar(name="x_1")
y = m.addVar(name="x_2")
m.update()

#Define the objective
m.setObjective(x - 2 * y, GRB.MINIMIZE)

#Add constraints
m.addConstr(-4 * x + 6* y <= 9, "xc")
m.addConstr(x + y <= 4, "yc")

#Added
m.addConstr(x <= 1, "e")
m.addConstr(y <= 2, "f")
m.addConstr(x >= 1, "fsdf")
######### END

m.optimize()
m.write("solution.sol")

if m.status == GRB.status.OPTIMAL:
    print "Found optimal solution"
else:
    print "No solution found"
    exit(0)