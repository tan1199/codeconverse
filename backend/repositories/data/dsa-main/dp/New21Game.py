class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [[] for i in range(10**4+2)]
        for i in range(k, 10**4+2):
            if(k<=n): dp[i] = [1, 0]
            else: dp[i] = [0, 1]
        
        start_index = k
        end_index = k-1+maxPts
        x_sum = sum(i[0] for i in dp[start_index:end_index+1])
        y_sum = sum(i[-1] for i in dp[start_index:end_index+1])
        print(x_sum, y_sum)

        for i in range(k-1, -1, -1):
            ans = [x_sum * 1/maxPts, y_sum * 1/maxPts]
            dp[i] = ans

            x_sum = x_sum + dp[start_index-1][0] - dp[end_index][0]
            y_sum = y_sum + dp[start_index-1][1] - dp[end_index][1]
            start_index-=1
            end_index-=1
        
        print(dp)
        return x_sum


        # cache = {}
        # def helper(num):
        #     if(num >= k):
        #         if(num>n): return [0, 1]
        #         return [1, 0]

        #     ans = [0, 0]
        #     for i in range(1, maxPts+1):
        #         x, y = helper(num + i)
        #         ans[0] += x * (1/maxPts)
        #         ans[-1] += y * (1/maxPts)

        #     cache[num] = ans
        #     return ans 
        
        # arr = helper(0)
        # return arr[0]

ans = Solution().new21Game(10000, 6666, 565)
print(ans)