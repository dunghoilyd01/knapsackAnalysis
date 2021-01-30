import knapsackR
import inputReader
import time

for i in range (1,4):
    W, n, wt, val, result = inputReader.input_processing("Test"+str(i)+".txt")
    a = knapsackR.knapsackRecursion(W, n, wt, val)
    time_start = time.time()
    a.Solve()
    print("Ket qua = ", a.ketqua, "| So phep toan = ", a.complexity)

