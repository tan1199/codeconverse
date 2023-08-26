class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
                
        maxArr = [[-1]*len(jobDifficulty)  for i in range(len(jobDifficulty))]
        
        for i in range(len(jobDifficulty)):
            maxArr[i][i] = jobDifficulty[i]
        
        for l in range(1, len(jobDifficulty)):
            for start in range(0, len(jobDifficulty)):
                if(l+start < len(maxArr)):
                    maxArr[start][start+l] = max(maxArr[start][start+l-1], maxArr[start+1][start+l])
                        
        cache = {}
        
        def getMin(index, d):
            
            if(d == 1): return maxArr[index][-1]
            if(d>len(jobDifficulty)): return -1
            
            key = (index, d)
            
            if(key in cache): return cache[key]
        
            prefixMax = -1
            best = 10**20
        
            for i in range(0, len(jobDifficulty[index:])-d+1):
                best = min(best, maxArr[index][index+i] + getMin(index + i + 1, d-1))
            
            cache[key] = best
            return best
        
        return getMin(0, d)
