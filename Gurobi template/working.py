from gurobipy import *
from collections import OrderedDict
from itertools import chain, combinations


def solve():
    m = Model("TSP0")
    m.setParam(GRB.param.Presolve, 0)
    m.setParam(GRB.param.Method, 0)
    m.setParam(GRB.param.MIPGap, 1e-7)

    ######### BEGIN: Write here your model for Task 1

    y = {}

    #Add variables to the model

    for i in range(1,4):
        y[i] = m.addVar(name="y_" + str(i))

    m.update()

    #Define the objective
    m.setObjective(147*y[1] + 210 * y[2] + 63 * y[3], GRB.MAXIMIZE)

    #Add constraints
    m.addConstr(2 * y[1] + 3 * y[2] + y[3] <= 5, "c_1")
    m.addConstr(3 * y[1] + 4 * y[2] + y[3] <= 7, "c_2")

    ######### END

    m.optimize()
    m.write("solution.lp")

    if m.status == GRB.status.OPTIMAL:
        print "Found optimal solution"
    else:
        print "No solution found"
        exit(0)


solve()

    





