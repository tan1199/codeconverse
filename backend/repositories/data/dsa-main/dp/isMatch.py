class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        sLen = len(s)
        pLen = len(p)
        
        @cache
        def dfs(sIndex, pIndex):
            # print(sIndex, pIndex)
            if(sIndex == sLen and pIndex == pLen): return True
            if(not (pIndex < pLen and p[pIndex] == "*") and ((sIndex == sLen) ^ (pIndex == pLen))): return False
            
            
            if(p[pIndex] == "?"): return dfs(sIndex+1, pIndex+1)
            if(p[pIndex] == "*"): 
                for index in range(sIndex, sLen+1):
                    if(dfs(index, pIndex+1)): return True
                return False
            
            if(s[sIndex]!= p[pIndex]): return False
            return dfs(sIndex+1, pIndex+1)
        
        return dfs(0, 0)
