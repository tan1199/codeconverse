class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
      
        arr2.sort()
        N = len(arr1)
        M = len(arr2)
        INF = 10**20

        @cache
        def helper(index1, prev):
            if(index1 == N): return 0
            
            best = INF
            if(arr1[index1] > prev): best = min(best, helper(index1 + 1, arr1[index1]))
            idx = bisect.bisect_right(arr2,prev)
            if(idx < M): best = min(best, 1 + helper(index1 + 1, arr2[idx]))
            return best

        res = helper(0, -1)    
        if(res == INF): return -1
        return res
