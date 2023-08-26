class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        if(nums1 == nums2):
            return 0
        
        if(k==0):
            return -1
        
        
        diff = [a-b for a,b in zip(nums1, nums2)]
        
        total = sum(diff)
        if(total != 0): return -1
        
        ans = 0
        for i in diff:
            if(i%k != 0):
                # print(i)
                return  -1
            if(i>0): ans += i//k
                
        return ans
