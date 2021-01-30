from ortools.algorithms import pywrapknapsack_solver
import inputReader
import time


for i in range (1,4):
    W, n, wt, val, result = inputReader.input_processing("Test" +str(i) + ".txt")
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    for CustomW in range (W, W + 50, 10):
        solver.Init(val, [wt], [CustomW])
        start_time = time.time()
        print("Ket qua Test", i,"voi CustomW: ", CustomW, "la: ",solver.Solve())
        print("Thoi gian hoan thanh Test", i, time.time()-start_time)

