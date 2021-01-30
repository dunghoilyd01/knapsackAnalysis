import knapsackDP
import knapsackR
import time

def file_convert(tenfile):
    with open(tenfile, 'r') as file:
        all_file = file.read().strip()
        all_file_list = all_file.split('\n')
        final_data = [[int(each_int) for each_int in line.split()] for line in all_file_list]  # make list of list and convert to int 
        return final_data
    

converted = file_convert("Input.txt")

n,W,result = converted[0]
wt = []
val = []

for i in range (1,n + 1):
    wt.append(converted[i][0])
    val.append(converted[i][1])
start_time1 = time.time()
recurresult = knapsackR.knapSack(W,wt,val,n)
recurtime = time.time() - start_time1
start_time2 = time.time()
dpresult = knapsackDP.knapSackDP(W,wt,val,n)
dptime = time.time() - start_time2
print("Thoi gian chay de quy: ", recurtime)
print("Thoi gian chay DP: ", dptime)

if (recurresult == result):
    print ("Knapsack de quy dung")
else:
    print("Knapsack de quy sai")

if (dpresult == result):
    print("Knapsack DP dung")
else:
    print("Knapsack DP sai")