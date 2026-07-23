class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        # In DFS:
        def dfs(r, c):
            # If the cell is out of bounds or is '0', return.
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            # Mark the current cell as '0' (visited).
            grid[r][c] = "0"
            # Recursively explore all 4 directions (up, down, left, right).
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        # Iterate through every cell in the grid.
        for r in range(rows):
            for c in range(cols):
                # When a cell with value '1' is found:
                if grid[r][c] == "1":
                    # Increment the island count.
                    # Run DFS from that cell.
                    dfs(r,c)
                    islands += 1
        # Continue until all cells are processed.
        # Return the total island count.
        return islands