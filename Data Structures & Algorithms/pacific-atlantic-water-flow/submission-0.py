from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        

        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True
                for nr, nc in get_neighbors(r, c, ocean):
                    queue.append((nr, nc))

        def get_neighbors(r, c, ocean):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                    neighbors.append((nr, nc))
            return neighbors

        pacific = []
        atlantic = []
        for c in range(cols):
            pacific.append((0, c)) # top of ocean
            atlantic.append((rows - 1, c)) #bottom of ocean
        
        for r in range(rows):
            pacific.append((r, 0)) # left of ocean
            atlantic.append((r, cols - 1)) # right of ocean
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res