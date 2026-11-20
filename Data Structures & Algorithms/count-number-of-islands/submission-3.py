from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS soln
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0]) # assuming atleast 1 cell
        num_islands = 0

        def bfs(r, c):
            q = deque() # to store candidates per level
            q.append((r, c)) # bcoz we want to enter until empty q loop
            grid[r][c] = "0" # mark visited

            while q:
                row, col = q.popleft() # first one we chose to investigate
                # grid[row][col] = "0" # so this doesn't work
                # check its neighbors
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or grid[nr][nc] == "0"):
                        continue

                    q.append([nr, nc])
                    # bcoz bfs is not called again and again
                    # we have to mark visited here
                    grid[nr][nc] = "0" # only this works


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    num_islands += 1

        return num_islands

        