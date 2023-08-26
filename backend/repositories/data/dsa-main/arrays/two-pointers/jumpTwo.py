class Solution:
    def jump(self, nums: List[int]) -> int:

        if(len(nums)==1): return 0

        count = 0
        start = 0
        end = 1

        while True:
            # print(nums[start:end], count)
            maxReach = start    
            while(start<end and start<len(nums)):
                maxReach = max(maxReach, start+nums[start])
                start += 1
            
            # print(maxReach)
            count += 1
            if(maxReach >= len(nums)-1): return count
            else: start, end = end, maxReach + 1
             


