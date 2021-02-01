class knapsackRecursion:
    complexity = 0
    wt = []
    val = []
    W = 0
    n = 0
    ketqua = 0
    def __init__ (self, W, n, wt, val):
        self.W = W
        self. wt = wt
        self. n = n
        self.val = val 
    def knapSack(self, W, n, wt, val):
        self.complexity += 2 
        if n == 0 or W == 0:
            return 0
        self.complexity += 1    
        if (wt[n-1] > W):  
            return self.knapSack(W, n - 1, wt, val) 
        else: 
            return max( 
                val[n-1] + self.knapSack( 
                    W-wt[n-1], n - 1, wt, val), 
                self.knapSack(W, n - 1, wt, val)) 
    
    def Solve(self):
        self.ketqua = self.knapSack(self.W, self.n, self.wt, self.val)
        
