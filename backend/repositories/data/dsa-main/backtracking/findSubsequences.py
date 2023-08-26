class Solution:

    def __init__(self):
        self.arr = None
        self.ans = set()

    def helper(self, cur, index):        
        if(index == len(self.arr) and len(cur)>1): 
            self.ans.add(tuple(i for i in cur))
            return
        
        if(index >= len(self.arr)): return
        
        if(len(cur)==0 or (cur[-1]<=self.arr[index])): 
            cur.append(self.arr[index])
            self.helper(cur, index+1)
            cur.pop()
        
        self.helper(cur, index+1)
        


    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.arr = nums
        self.helper([], 0)
        return self.ans
