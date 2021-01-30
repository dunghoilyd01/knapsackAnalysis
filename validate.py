import inputReader
import knapsackDP
import knapsackR

validDP = 1
validR = 1
for i in range(1,4):
    W, n, wt, val, result = inputReader.input_processing("Test"+str(i)+".txt")
    DP = knapsackDP.knapsackDP(W, n, wt, val)
    R = knapsackR.knapsackRecursion(W, n, wt, val)
    DP.Solve()
    R.Solve()
    if (DP.ketqua != result):
        validDP = 0
        print("DP SAI VOI TEST ", i)
    if (R.ketqua != result):
        validR = 0
        print("DE QUY SAI VOI TEST ",i)
if (validDP):
    print("DP dung cho moi test")
if (validR):
    print ("De quy dung cho moi test")
