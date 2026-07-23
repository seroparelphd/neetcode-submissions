class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        islands = 0
        
        def dfs(row, col):
            if col < 0 or row < 0 or col >= n or row >= m or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands