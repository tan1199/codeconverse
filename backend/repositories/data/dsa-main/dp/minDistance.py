class Solution:
    def __init__(self):
        self.s1 = None
        self.s2 = None
        self.cache = {}


    def helper(self, index1, index2):
        key = (index1, index2)
        if(key  in self.cache): return self.cache[key]

        if(index1 == len(self.s1)): return len(self.s2) -index2
        if(len(self.s2) == index2): return len(self.s1) - index1
        if(self.s1[index1] == self.s2[index2]): ans = self.helper(index1+1, index2+1)
        else: ans = min(self.helper(index1, index2+1) +1, self.helper(index1+1, index2) +1, self.helper(index1+1, index2+1) +1)

        self.cache[key] = ans
        return ans

    def minDistance(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2
        return self.helper(0, 0)
