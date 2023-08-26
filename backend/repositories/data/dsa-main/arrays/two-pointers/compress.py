class Solution:
    def compress(self, chars: List[str]) -> int:

        def getLen(num):
            ans = []
            if num == 1: return ans
            while(num):
                ans.append(str(num%10))
                num = num//10
            return ans[::-1]
        
        def replace(arr, swap, index):
            for i, val in enumerate(swap):
                if(index+i < len(arr)): arr[index+i] = val
                else: arr.append(val)

        index = 0
        start = 0
        end = 0
        while(start<len(chars)):
            while(end<len(chars) and chars[end] == chars[start]): end+=1
            
            chars[index] = chars[start]
            index+=1

            arr = getLen(end-start)
            replace(chars, arr, index)
            
            index+=len(arr)
            start = end

        return index
