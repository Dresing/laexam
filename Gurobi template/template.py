from gurobipy import *
from collections import OrderedDict
from itertools import chain, combinations


def solve():
    m = Model("TSP0")
    m.setParam(GRB.param.Presolve, 0)
    m.setParam(GRB.param.Method, 0)
    m.setParam(GRB.param.MIPGap, 1e-7)

    ######### BEGIN: Write here your model for Task 1

    edges = {}

    #Add variables to the model

    #for edge in E:
        #edges[edge[0], edge[1]] = m.addVar(name="x" + str(edge[0]) + "_" + str(edge[1]), ub=1)

    m.update()

    #Define the objective
    #m.setObjective(quicksum(edges[e[0], e[1]] * distance(points[e[0]], points[e[1]]) for e in E), GRB.MINIMIZE)

    #Add constraints
    #for i in V:
        #m.addConstr(quicksum(edges[k, l] for (k, l) in E if k == i or l == i) == 2, "dc_" + str(i))

    ######### END

    m.optimize()
    m.write("solution.lp")

    if m.status == GRB.status.OPTIMAL:
        print "Found optimal solution"
    else:
        print "No solution found"
        exit(0)


solve()

    





