class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        mod = 10**9 + 7

        @cache
        def helper(index):
            if(index == len(s)): return 1
            if(s[index] == '0'): return 0

            count = 0
            cur = 0
            for ind in range(index, len(s)):
                cur *= 10 
                cur += int(s[ind])
                if(cur > k): break

                count = (count%mod +  helper(ind+1)%mod)%mod
            return count

        return helper(0)
