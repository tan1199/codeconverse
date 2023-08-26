class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        N = len(days)
        days.sort()

        @cache
        def helper(index):
            if(index >= N): return 0
            curday = days[index]

            ans = 10**10
            ans = min(ans, helper(index+1)+costs[0])
            
            while(index<N and days[index]-curday<7): index+=1 
            ans = min(ans, helper(index) + costs[1])
            
            while(index<N and days[index]-curday<30): index+=1 
            ans = min(ans, helper(index) + costs[2])
            return ans

        return helper(0)
