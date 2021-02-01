import knapsackDP
import inputReader
import time

for i in range (1,4):
    W, n, wt, val, result = inputReader.input_processing("Test"+str(i)+".txt")
    for CustomW in range (W, W + 50, 10):
        a = knapsackDP.knapsackDP(CustomW, n, wt, val)
        start_time = time.time()
        a.Solve()
        print("Test case: ",i, "Custom W:", CustomW)
        print("Giai bai toan trong:",time.time() - start_time)
        print("Voi so phep toan: ", a.complexity)

