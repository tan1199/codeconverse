class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        arr = []
        for val, freq in groupby([i for i in s]):
            arr.append([val, len(list(freq))])        


        N = len(arr)

        if(N == 1): return 0
        start = 1 if(arr[0][0] == '0') else 0
        end = N-1 if(arr[-1][0] == '0') else N-2
        if(start>end): return 0

        zero = 0
        one = 0
        prefix = []
        for i in range(start, end, 2):
            one += arr[i][1]
            zero += arr[i+1][1]
            prefix.append([one, zero])
        
        ans = 10**10
        for i in range(len(prefix)):
            ans = min(ans, prefix[i][0] + prefix[-1][1]-prefix[i][1])
        
        ans = min(ans, prefix[-1][0])
        ans = min(ans, prefix[-1][1])
        return ans
