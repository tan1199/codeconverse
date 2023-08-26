class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False]*M for _ in range(N)]
        mod = 10**9 + 7

        @cache
        def dfs(row_index, col_index):
            ans = 1
            cur = grid[row_index][col_index]
            for dx, dy in dir:
                newx, newy = row_index + dx, col_index + dy
                if(newx < 0  or newx >= N or newy < 0 or newy >= M): continue
                if(grid[newx][newy] <= cur): continue  
                ans = (ans%mod + dfs(newx, newy)%mod)%mod
            return ans
        
        ans = 0
        for row_index in range(N):
            for col_index in range(M):
                ans = (ans%mod + dfs(row_index, col_index)%mod)%mod
        
        return ans
