class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = 0
        count = [0 for i in range(66)]
        
        for num in nums:            
            index = 0
            while(num):
                if(num%2 == 1): count[index] += 1
                index+=1
                num >>= 1
            
        
        def op(nums, k):
            
            bor = 0
            for num in nums: bor = bor | num
            best = [-1, -1]
            
            for idx, num in enumerate(nums):
                temp = num
                cur = bor

                index = 0
                while(temp):
                    if(temp%2 == 1 and count[index]==1):
                        cur = cur ^ (1<<index)
                    index += 1
                    temp >>= 1

                cur = cur | (num<<k)
                if(best[0]<cur): best = [cur, idx]
            
            return best
            # idx = best[-1]
            
            # num = nums[idx]
            # index = 0
            # while(num):
            #     if(num%2==1): count[index]-=1
            #     index+=1
            #     num >>= 1
                
                
            # nums[idx] *= 2
            
            # num = nums[idx]
            # index = 0
            # while(num):
            #     if(num%2==1): count[index]-=1
            #     index+=1
            #     num >>= 1
                
        val, index = op(nums, k)
        return val
        # ans = 0
        # for i in nums: ans |= i
        # return ans
                
# if you observer you will see the shift (<<1) is always done on the same index to get the maximum OR
