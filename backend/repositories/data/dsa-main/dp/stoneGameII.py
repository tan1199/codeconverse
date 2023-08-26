class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        def helper(index, M):
            if(index>=len(piles)): return 0
            rem_piles = len(piles) - index
            if(rem_piles<=2*M): return sum(piles[index:])
            
            ans = -10**10
            running_sum = 0
            for i in range(2*M):
                running_sum += piles[index+i]
                ans = max(ans, running_sum - helper(index+i+1, max(M, i+1)))
            
            return ans
        
        return (sum(piles) + helper(0, 1))//2
