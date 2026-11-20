class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0]) # assuming atleast 1 cell
        num_islands = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if (row < 0 or row >= ROWS or
                    col < 0 or col >= COLS):
                    continue
                if grid[row][col] == "1":
                    dfs(row, col)
                    

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands
