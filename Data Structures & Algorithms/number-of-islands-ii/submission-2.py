import copy

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [['0' for _ in range(n)] for _ in range(m)]  # [[0, 0]]

        def numIslands(grid: List[List[str]]) -> int:
            m, n = len(grid), len(grid[0])
            num_islands = 0

            def dfs(row, col):
                if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                    return
                else:
                    grid[row][col] = '0'
                    dfs(row, col + 1) # right
                    dfs(row + 1, col) # down
                    dfs(row, col - 1) # left
                    dfs(row - 1, col) # up

            for row in range(m):
                for col in range (n):
                    if grid[row][col] == '1':
                        num_islands += 1
                        dfs(row, col)

            return num_islands
        output = []
        for i in range(len(positions)):
            # print(grid)
            grid[positions[i][0]][positions[i][1]] = '1'
            grid2 = copy.deepcopy(grid)
            output.append(numIslands(grid2))
            # print(grid)
        return output

