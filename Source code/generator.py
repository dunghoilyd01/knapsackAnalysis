import random
from ortools.algorithms import pywrapknapsack_solver

def generator(W, n, filename = None, output = None):
    wt = []
    val = []
    for i in range (n):
        wt.append(random.randrange(100))
        val.append(random.randrange(100))

    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    solver.Init(val, [wt], [W])
    bestvalue = solver.Solve()
    if filename:
        file = open(filename,"w")
        file.write(str(n) + " " + str(W) + " " + str(bestvalue) + "\n")
        for i in range (n):
            file.write(str(wt[i]) + " " + str(val[i])+ "\n")
    if output != None:
        print("W = ",W)
        print("n = ", n)
        print("wt = ", wt)
        print("val = ",val)
    return wt,val,bestvalue

