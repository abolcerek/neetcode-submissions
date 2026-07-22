from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0


        def BFS(starting_row, starting_col):
            area = 1
            queue = deque()
            visited = set()
            queue.append((starting_row, starting_col))
            visited.add((starting_row, starting_col))
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    row, col = queue.popleft()
                    for nr, nc in get_neighbors(row, col):
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            area += 1
            return area


        
        def get_neighbors(row, col):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    neighbors.append((nr, nc))
            return neighbors



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    curr_area = BFS(i, j)
                    max_area = max(max_area, curr_area)
        return max_area