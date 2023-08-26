class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        def getNumOfOnBits(num):
            ans = 0
            while(num):
                ans += 1
                num = num & (num-1)
            return ans
        
        ans = 0
        zero_one = ((a | b) ^ c) & c
        ans += getNumOfOnBits(zero_one)
        
        one_zero_a = ((a | b) ^ c) & a
        ans += getNumOfOnBits(one_zero_a)

        one_zero_b = ((a | b) ^ c) & b
        ans += getNumOfOnBits(one_zero_b)

        return ans
