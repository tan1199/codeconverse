class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1 for i in range(len(prices))]
        
        index = 1
        
        while(index<len(prices)):
            if(prices[index] + 1 == prices[index-1]):
                dp[index] = dp[index-1] + 1
            index = index+1
        
        return sum(dp)
