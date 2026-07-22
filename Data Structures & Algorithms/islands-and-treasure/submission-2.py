from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            distance = 1
            visited = set()
            visited.add((r, c))
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    row, col = queue.popleft()
                    for nr, nc in get_neighbors(row, col):
                        if grid[nr][nc] == 0:
                            return distance
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                distance += 1


        def get_neighbors(row, col):
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    neighbors.append((nr, nc))
            return neighbors





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    distance = bfs(r, c)
                    grid[r][c] = distance