class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        
        N = len(nums)
        map = defaultdict(list)
        for index, num in enumerate(nums): map[num].append(index)
        
        def cov(indexs):
            if(len(indexs) <= 1): return 10 ** 10
            
            ans = 0
            for index in range(1, len(indexs)):
                ans = max(ans, indexs[index] - indexs[index-1])
            ans = max(ans, indexs[0] -  indexs[-1] + N)
            return ans
            
        
        
        val, minCov = -1, 10**10 + 1
        for num in map:
            re = cov(map[num])
            if(re < minCov):
                val = num
                minCov = re
        
        
        print(val)
        
        def can(s):
            nonlocal val
            counter = defaultdict(int)
            start = N - s
            end = start + 2*s
            # print(s, start, end)
            for index in range(start, end+1):  counter[nums[index%N]] += 1
                
            for index in range(N):
                # print(index, counter)
                if(counter[val] == 0): return False
                counter[nums[start%N]] -= 1
                start += 1
                end += 1
                counter[nums[end%N]] += 1
            
            return True
            
            
        low = 0
        high = len(nums)//2 + 1
        while(low<high):
            # print(low, high)
            mid = (low + high)//2
            if(can(mid)): high = mid
            else: low = mid + 1
        return low
