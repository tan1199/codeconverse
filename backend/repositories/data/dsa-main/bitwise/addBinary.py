class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def binToInt(s):
            num = 0
            for i in s:
                num = num << 1
                if( i == '1'): num = num | 1
            
            return num
        
        def intToBin(num):
            if(num == 0): return "0"
            ans = ""
            while(num):
                ans += str(num%2)
                num = num//2
            return ans[::-1]


        a = binToInt(a)
        b = binToInt(b)
        # print(a, b)
        return intToBin(a+b)

