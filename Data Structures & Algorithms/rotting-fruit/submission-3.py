from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # DFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0]) # assuming atleast 1 cell
        fresh = 0
        steps = 0

        # def dfs(r, c):
        #     for dr, dc in directions:
        #         row = r + dr
        #         col = c + dc
        #         steps += 1

        #         if (row < 0 or row >= ROWS or
        #             col < 0 or col >= COLS):
        #             continue
        #         else:
        #             if grid[row][col] == "0":
        #                 continue
        #             elif grid[row][col] == "1":
        #                 fresh -= 1
        #                 dfs(row, col)
        #             elif grid[row][col] == "2":
        #                 continue
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append((r, c))

        print(fresh)
        print(q)

        while fresh > 0 and q:

            length = len(q)
            for wave in range(length):
                row, col = q.popleft()

                # check neighbors
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # valid cell?
                    if (r >= 0 and r < ROWS
                        and c >= 0 and c < COLS):
                        # yes valid cell
                        if grid[r][c] == 1:
                            fresh -= 1 # reduce fresh count
                            grid[r][c] = 2 # turn to rotten
                            # add for next wave
                            q.append((r,c))

            steps += 1

        if fresh > 0:
            return -1

        return steps
