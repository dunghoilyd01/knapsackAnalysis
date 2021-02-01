def file_convert(tenfile):
    with open(tenfile, 'r') as file:
        all_file = file.read().strip()
        all_file_list = all_file.split('\n')
        final_data = [[int(each_int) for each_int in line.split()] for line in all_file_list]
        return final_data

def input_processing(tenfile):
    converted = file_convert(tenfile)
    n,W,result = converted[0]
    wt = []
    val = []
    for i in range (1,n + 1):
        wt.append(converted[i][0])
        val.append(converted[i][1])
    return W, n, wt, val, result
    