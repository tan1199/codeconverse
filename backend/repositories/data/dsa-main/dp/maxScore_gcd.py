class Solution:
    def maxScore(self, nums: List[int]) -> int:

        N = len(nums)
        s = set([index for index in range(N)])

        def gcd(a, b):
            if(a<b): return gcd(b, a)
            return a if(b==0) else gcd(b, a%b)

        @cache
        def helper(visited, i):
            ans = 0

            for index1 in range(len(nums)):
                for index2 in range(index1+1, len(nums)):
                    if( ((visited>>index1)%2 == 1) or ((visited>>index2)%2==1) ): continue
                    
                    visited |= 1<<index1
                    visited |= 1<<index2
                    ans = max(ans, i*gcd(nums[index1], nums[index2]) + helper(visited, i+1))
                    visited ^= 1<<index1
                    visited ^= 1<<index2
            return ans
        
        visited = 0        
        ans = helper(visited, 1)
        return ans

# [1,2]
# [3,4,6,8]
# [1,2,3,4,5,6]
# [111111, 222222, 333333, 444444, 555555 ,66666]
# [773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730]
# [7,3,1,2,9,4,3,7,9,8,3,9]
