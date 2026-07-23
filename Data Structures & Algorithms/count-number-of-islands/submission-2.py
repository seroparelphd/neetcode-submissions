class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        # In BFS:
        def bfs(r, c):
            q = deque()
            # Push the starting cell into a queue and mark it as '0'.
            grid[r][c] = '0'
            q.append((r, c))
            # While the queue is not empty:
            while q:
                # Pop a cell.
                row, col = q.popleft()
                # Explore its 4 neighbors (up, down, left, right).
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0'):
                        continue
                    # If a neighbor is land, mark it as '0' and add it to the queue.
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        # Traverse every cell in the grid.
        for r in range(rows):
            for c in range(cols):
                # When a '1' (land) cell is found:
                if grid[r][c] == '1':
                    # Increment the island count.
                    islands += 1
                    # Start BFS from that cell.
                    bfs(r, c)

                
        # Continue scanning the grid.
        # Return the total number of islands.
        return islands