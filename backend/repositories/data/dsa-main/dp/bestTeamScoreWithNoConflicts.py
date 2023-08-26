class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        arr = [[score, age] for score,age in zip(scores, ages)]
        arr.sort() # O(nlogn)
        dp = [None for i in range(len(scores))]
        dp[0] = arr[0][0]

        # O(n^2)
        for index in range(len(scores)):
            curmax = arr[index][0]
            cur_age = arr[index][1]
            for j in range(index-1, -1,-1):
                if(cur_age >= arr[j][-1]): 
                    curmax = max(curmax, arr[index][0] + 
            dp[index] = curmax
        return max(dp)
