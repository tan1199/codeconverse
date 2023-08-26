class Solution:
    def answerQueries(self, arr: List[int], queries: List[int]) -> List[int]:
        arr.sort()
        N = len(arr)
        for i in range(1, N): arr[i] += arr[i-1]


        def binarySearch(num, low=0 , high=N-1):
            if(low>high): return low
            mid = low + (high - low)//2
            if(arr[mid] == num): return mid+1
            if(arr[mid]>num): return binarySearch(num, 0, mid-1)
            return binarySearch(num, mid+1, high)
        
        return list(map(binarySearch, queries))
