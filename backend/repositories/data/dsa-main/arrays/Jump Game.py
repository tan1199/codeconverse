class Solution:
    def canJump(self, nums: List[int]) -> bool:
    
        curIndex = 0
        allowed = curIndex + nums[0]

        while(curIndex<=allowed and curIndex<len(nums)):
            allowed = max(allowed, curIndex + nums[curIndex])
            curIndex+=1
        
        # print(curIndex)
        return curIndex == len(nums)
