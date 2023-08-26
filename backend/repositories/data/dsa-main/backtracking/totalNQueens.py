class Solution:
    def totalNQueens(self, n: int) -> int:


        def good(row_index, col_index, cur):
            for val in cur:
                if(val & 1<<col_index): return False
            
            for index in range(1, row_index+1):
                val = 0
                if(col_index-index >=0 ): val = val | (1<<(col_index-index))
                if(0 <= col_index+index < n): val = val | (1<<(col_index+index))

                if(cur[row_index-index] & val): return False
            
            return True




        def helper(row_index, cur):
            if(row_index == n): return 1
            ans = 0
            for col_index in range(n):
                if(good(row_index, col_index, cur)):
                    cur[row_index] = 1<<col_index
                    ans += helper(row_index+1, cur)
                    cur[row_index] = 0
            
            return ans

        cur = [0 for i in range(n)]
        return helper(0, cur)
