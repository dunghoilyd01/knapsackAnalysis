import random
from ortools.algorithms import pywrapknapsack_solver

n = random.randrange(50,60)
W = random.randrange(60,70)
wt = []
val = []

for i in range (n):
    wt.append(random.randrange(50))
    val.append(random.randrange(50))

solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

solver.Init(val, [wt], [W])
bestvalue = solver.Solve()
file = open("Input.txt","w")
file.write(str(n) + " " + str(W) + " " + str(bestvalue) + "\n")
for i in range (n):
    file.write(str(wt[i]) + " " + str(val[i])+ "\n")
print("W = ",W)
print("n = ", n)
print("wt = ", wt)
print("val = ",val)
