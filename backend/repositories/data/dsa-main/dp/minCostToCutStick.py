class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        N = len(cuts)
        cuts.sort()


        @cache
        def helper(start_index, end_index, cstart, cend):
            if(start_index == end_index): return 0
            if(cstart == cend): return end_index - start_index
            if(cstart>cend): return 0

            ans = 10**10
            cur_cost = end_index - start_index
            for index in range(cstart, cend+1):
                ans = min(ans, cur_cost + helper(start_index, cuts[index], cstart, index-1) + helper(cuts[index], end_index, index+1, cend))
            return ans

        return helper(0, n, 0, N-1)
