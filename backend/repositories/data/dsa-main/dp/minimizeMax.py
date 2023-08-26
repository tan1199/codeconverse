class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if(p == 0): return 0

        N = len(nums)
        nums.sort()
        inf = 10**10 +1

        prevprev = [inf for i in range(p + 1)]
        prev = [inf for i in range(p + 1)]
        dp = [inf for i in range(p + 1)]
        
        for index in range(N-2, -1, -1):
            for p_index in range(1, p+1):
                if(N - index < 2*p_index): continue
                if( p_index == 0): continue
                if(p_index == 1):
                    dp[p_index] = min(prev[p_index], nums[index+1] - nums[index])
                    continue

                dp[p_index] = min(
                    max(nums[index+1] - nums[index], prevprev[p_index-1]),
                    prev[p_index]
                )

            prevprev = prev
            prev = dp
            dp = [inf for i in range(p + 1)]
            
        return prev[-1]

# best solution for the problem is using binary search ckeck the problem (2616. leetcode)
# with a mix of greedy.
