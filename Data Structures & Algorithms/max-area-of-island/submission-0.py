from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def BFS(r, c):
            queue = deque()
            arr = 1
            queue.append((r, c)) #we add the start node to the queue
            visited = set() #we add the start node to visited
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                for nr, nc in get_neighbors(row, col):
                    if (nr, nc) not in visited:
                        arr += 1
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return arr        

        def get_neighbors(row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    neighbors.append((nr, nc))
            return neighbors
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    resp_area = BFS(r, c) #return the area we find
                    area = max(area, resp_area)
        return area