class Solution:

    def getNumOfCombinations(self, mn, mx, index1, index2, start, end):
        if(index1>=len(mn) or index2>=len(mx)): return 0
        mn_idx, mx_idx = min(mn[index1], mx[index2]), max(mn[index1], mx[index2])

        left = mn_idx - start + 1
        right = end - mx_idx
        if(mn_idx == mn[index1]): ans = self.getNumOfCombinations(mn, mx, index1+1, index2, mn[index1]+1, end)
        else: ans = self.getNumOfCombinations(mn, mx, index1, index2+1, mx[index2]+1, end)

        return (left*right) + ans

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        def getSubAns(nums, start, end):
            mn = []
            mx = []
            for i in range(start, end): 
                if(nums[i] == minK): mn.append(i)
                if(nums[i] == maxK): mx.append(i)

            if((len(mn)==0 or len(mx)==0)): return 0
            
            # if we have n minK and m maxK in [start, end)
            # how to get all possible combinations
            return self.getNumOfCombinations(mn, mx, 0, 0, start, end)

        start = 0
        end = 0
        ans = 0 

        while(end<len(nums)):
            while(end<len(nums) and minK<=nums[end]<=maxK): end += 1
            ans += getSubAns(nums, start, end)
            end += 1
            start = end
        
        return ans

            


            
