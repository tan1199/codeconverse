class Solution:
        
    pizza = []
    M = 0
    N = 0
    prefixSum = []
    cache = {}
    mod = 10**9 + 7
    
    def ways(self, pizza: List[str], k: int) -> int:
        
        self.pizza = pizza
        self.M = len(pizza) - 1
        self.N = len(pizza[0]) - 1
        self.cache = {}
        
        prefixSum = [[0]*len(pizza[0]) for i in range(len(pizza))]
        
        
        prefixSum[0][0] = 1 if(pizza[0][0]=='A') else 0
        
        for i in range(1, len(pizza[0])): 
            prefixSum[0][i] += prefixSum[0][i-1]
            prefixSum[0][i] += 1 if(pizza[0][i]=='A') else 0
        
        for i in range(1, len(pizza)): 
            prefixSum[i][0] += prefixSum[i-1][0]
            prefixSum[i][0] += 1 if(pizza[i][0]=='A') else 0
        
        
        for i in range(1, len(pizza)):
            for j in range(1, len(pizza[0])):
                prefixSum[i][j] += 1 if(pizza[i][j]=='A') else 0
                prefixSum[i][j] += prefixSum[i-1][j]
                prefixSum[i][j] += prefixSum[i][j-1]
                prefixSum[i][j] -= prefixSum[i-1][j-1]
                
        if(prefixSum[-1][-1]<k): return 0
        
        self.prefixSum = prefixSum
        return self.helper(0,0,k)
    
    
    def helper(self, rowIndex, colIndex, k):
        
        key = (rowIndex, colIndex, k)
        if(key in self.cache): return self.cache[key]
        
        ans = 0
        
        if(k == 1): return self.valid(rowIndex, self.M, colIndex, self.N)
        
        for index in range(rowIndex+1, self.M+1):
            ans += self.valid(rowIndex, index-1, colIndex, self.N) * self.helper(index, colIndex, k-1)
            ans = ans%self.mod
        
        for index in range(colIndex+1, self.N+1):
            ans += self.valid(rowIndex, self.M, colIndex, index-1) * self.helper(rowIndex, index, k-1)
            ans = ans%self.mod

        self.cache[key] = ans
        return ans
    
    def valid(self, rowStart, rowEnd, colStart, colEnd):        
        ans = self.prefixSum[rowEnd][colEnd]
        
        if(rowStart-1 >= 0):
            ans -= self.prefixSum[rowStart-1][colEnd]
            
        if(colStart-1 >= 0):
            ans -= self.prefixSum[rowEnd][colStart-1]
        
        if(rowStart-1 >= 0 and colStart-1 >= 0):
            ans += self.prefixSum[rowStart-1][colStart-1]
        
        return 1 if(ans>0) else 0

        
        
        



            
        
        
