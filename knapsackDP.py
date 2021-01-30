class knapsackDP:
    W = 0
    n = 0
    wt = []
    val = []
    sosanh = 0
    gan = 0
    duyetmang = 0
    ketqua = 0
    def __init__(self, W, n, wt, val):
        self.W = W
        self.n = n
        self. wt = wt
        self.val = val

    def knapSack(self, W, n, wt, val): 
        DEFAULTSPACEUSAGE = (W + 1) * (n + 1)
        self.duyetmang += DEFAULTSPACEUSAGE
        self.gan += DEFAULTSPACEUSAGE
        K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
        self.sosanh += DEFAULTSPACEUSAGE
        for i in range(n + 1):
            for w in range(W + 1):
                self.sosanh += 2 
                if i == 0 or w == 0: 
                    K[i][w] = 0
                    self.gan += 1
                elif wt[i-1] <= w: 
                    self.sosanh += 1
                    K[i][w] = max(val[i-1] 
                              + K[i-1][w-wt[i-1]],   
                                  K[i-1][w])
                    self.gan += 1 
                else: 
                    K[i][w] = K[i-1][w] 
                    self.gan += 1
        return K[n][W] 
    
    def Solve(self):
        self.ketqua = self.knapSack(self.W, self.n, self.wt, self.val)

  
W =  64
n =  53
wt =  [1, 6, 38, 16, 8, 23, 23, 46, 19, 41, 20, 32, 46, 25, 41, 5, 49, 1, 16, 46, 7, 34, 40, 5, 4, 45, 16, 13, 13, 45, 46, 15, 42, 22, 32, 15, 18, 17, 31, 10, 38, 28, 46, 33, 1, 7, 5, 48, 20, 39, 1, 12, 35]
val =  [9, 10, 48, 8, 34, 12, 34, 47, 39, 14, 13, 0, 45, 30, 39, 41, 4, 26, 42, 44, 3, 45, 8, 47, 38, 24, 47, 22, 13, 48, 8, 0, 33, 41, 3, 7, 34, 33, 38, 22, 3, 37, 8, 0, 25, 26, 42, 30, 0, 38, 13, 23, 42]

a = knapsackDP(W, n, wt, val)
a.Solve()
print(a.ketqua)
print(a.gan+a.sosanh+a.duyetmang)