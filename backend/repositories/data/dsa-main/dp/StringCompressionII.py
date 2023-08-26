class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def f(x):
            if(x==0): return 0
            if(x==1): return 1
            if(x<=9): return 2
            if(x<=99): return 3
            return 4
        
        cache = {}
        
        def getMin(index, prevChar, run, k):
            
            key = (index, prevChar, run, k)
            
            if key in cache:
                return cache[key]
            
            if(index>=len(s)): return f(run)
            
            best = 10**20
            
            if(s[index] == prevChar):
                #keep
                best = min(best, getMin(index+1, prevChar, run+1, k))
                
                #remove
                if(k>0):
                    best = min(best, getMin(index+1, prevChar, run, k-1))
            
            else:
                #keep
                best = min(best, getMin(index+1, s[index], 1, k) + f(run))
                
                #remove
                if(k>0):
                    best = min(best, getMin(index+1, prevChar, run, k-1))
            
            cache[key] = best
            return best
        
        return getMin(0, '', 0, k)
