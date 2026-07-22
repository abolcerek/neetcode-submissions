from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def BFS(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for nr, nc in get_neighbors(row, col):
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))


        def get_neighbors(row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    neighbors.append((nr, nc))
            return neighbors



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    BFS(r, c)
                    islands += 1
        return islands
