class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0 for i in range(high+1)]
        dp[one] += 1
        dp[zero] += 1

        mod = 10**9 + 7

        for index in range(high+1):
            if(index-one>=0): dp[index] = (dp[index]%mod + dp[index-one]%mod)%mod
            if(index-zero>=0): dp[index] = (dp[index]%mod + dp[index-zero]%mod)%mod
        
        ans = 0
        for val in dp[low:high+1]: ans = (ans%mod + val%mod)%mod
        
        return ans

