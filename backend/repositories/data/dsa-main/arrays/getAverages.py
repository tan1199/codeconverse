class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        N = len(nums)

        if(N < 2*k+1): return [-1]*N
        if(k==0): return nums

        ans = []
        prefix_sum = 0
        index = 0

        while(index <= 2*k and index<N):
            prefix_sum += nums[index]
            index += 1
        
        start = 0
        ans.append(prefix_sum//(2*k+1))

        while(index < N):
            prefix_sum += nums[index]
            prefix_sum -= nums[start]
            ans.append(prefix_sum//(2*k+1))
            index += 1
            start += 1
        
        return [-1]*k + ans + [-1]*k
