from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        initial_queue = deque()

        def BFS(initial_queue, fresh):
            minutes = 0
            queue = deque()
            visited = set()
            for _ in range(len(initial_queue)):
                val = initial_queue.popleft()
                visited.add(val)
                queue.append(val)
            while fresh > 0 and queue:
                level_size = len(queue)
                for _ in range(level_size):
                    row, col = queue.popleft()
                    neighbors = get_neighbors(row, col)
                    for nr, nc in neighbors:
                        if (nr, nc) not in visited:
                            grid[nr][nc] = 2
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            fresh -= 1
                minutes += 1
            return fresh, minutes
        
        def get_neighbors(row, col):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = []

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    neighbors.append((nr, nc))
            return neighbors

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    initial_queue.append((r, c))
        new_fresh, mins = BFS(initial_queue, fresh)
        if new_fresh == 0:
            return mins
        else:
            return -1      

        

        