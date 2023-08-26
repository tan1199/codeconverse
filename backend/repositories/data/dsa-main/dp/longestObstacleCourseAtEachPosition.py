class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        N = len(obstacles)
        dp = [1 for i in range(N)]
        best = []

        for index, height in enumerate(obstacles):
            low = 0
            high = len(best)-1

            while(low<=high):
                mid = low + (high - low)//2
                if(best[mid] <= height): low = mid+1
                else: high = mid-1
            
            if(low < len(best)): best[low] = height
            else: best.append(height)
            dp[index] = low+1
        
        return dp
