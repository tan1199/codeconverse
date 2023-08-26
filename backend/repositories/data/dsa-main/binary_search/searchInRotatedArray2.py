class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if(nums[-1] == target): return True
        while(nums and nums[-1] == nums[0]): nums.pop()
        if(not nums): return False

        N = len(nums)
        '''
            [x x x x x+1 x+2 .. x+k x-3 x-2 x-1 x x x x]
        '''

        def good(index):
            if(nums[index] >=  nums[0]):
                if(nums[0] <= target <= nums[index]): return True
                return False
            else:
                if(target > nums[-1] or target < nums[index]): return True
                return False
            
            return False

        low = 0
        high = N-1

        while(low < high):
            mid = low + (high - low)//2
            if(nums[mid] == target): return True
            # print(low, high, mid)

            # good(mid) => true means target in [0...mid]
            if(good(mid)): high = mid
            else: low = mid+1
        
        return (0 <= low < N and nums[low] == target) 
