class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        
        running_xor = 0
        visited = defaultdict(int)
        visited[running_xor] = 1
        ans = 0
        
        for index, num in enumerate(nums):
            running_xor ^= num
            if(running_xor in visited): ans += visited[running_xor]
            visited[running_xor] += 1
        
        return ans
        
