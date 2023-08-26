class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:

        N = len(dp)
        M = len(dp[0])

        for i in range(1, N): dp[i][0] += dp[i-1][0]
        for i in range(1, M): dp[0][i] += dp[0][i-1]

        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
