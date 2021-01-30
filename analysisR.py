import knapsackR
import generator




for W in range (80,150,10):
    wt,val,result = generator.generator(W,80)
    a = knapsackR.knapsackRecursion(W,80,wt,val)
    a.Solve()
    print("n = ", 80,"W = ", W, "complexity = ",a.complexity)

