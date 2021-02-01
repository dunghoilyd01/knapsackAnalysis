class knapsackDP:
    W = 0
    n = 0
    wt = []
    val = []
    sosanh = 0
    gan = 0
    duyetmang = 0
    ketqua = 0
    complexity = 0
    def __init__(self, W, n, wt, val):
        self.W = W
        self.n = n
        self. wt = wt
        self.val = val

    def knapSack(self, W, n, wt, val): 
        DEFAULTSPACEUSAGE = (W + 1) * (n + 1)
        self.sosanh += DEFAULTSPACEUSAGE
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
                    self.sosanh += 1
                    K[i][w] = K[i-1][w] 
                    self.gan += 1
        return K[n][W] 
    
    def Solve(self):
        self.ketqua = self.knapSack(self.W, self.n, self.wt, self.val)
        self.complexity = self.gan + self.sosanh
