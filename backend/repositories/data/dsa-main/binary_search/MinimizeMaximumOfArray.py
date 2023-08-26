class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        def isValid(target):
            carry = 0
            
            for index in range(len(nums)-1,-1,-1):
                cur = nums[index]
                cur += carry
                carry = 0
                if(cur>target):
                    carry = cur - target
                    
            return carry == 0
        
        left = 0
        right = 10**9
        
        while left<right:
            mid = (left+right)//2
            
            # print(mid, isValid(mid))
            
            if(isValid(mid)):
                right = mid
            else:
                left = mid+1
                
        # print(left,right)
        return right
        
