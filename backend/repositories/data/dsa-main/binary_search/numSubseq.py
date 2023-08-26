class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        N = len(nums)
        start = 0
        end = N-1
        mod = 10**9 + 7
        dp = {}

        def binarySearch(start, end):
            s = start

            while(start<=end):
                mid = start + (end - start +1)//2
                if(nums[s] + nums[mid] <= target):
                    if(start == end): return start 
                    start = mid
                else: end = mid-1
            
            return -1

        def getpow(num):
            if(num in dp): return dp[num]
            dp[num] = 2**num
            return dp[num]

        count = 0
        while(start<N):
            end = binarySearch(start, end)
            if(end == -1): break
            count += getpow(end - start)
            start += 1

        return count%mod
