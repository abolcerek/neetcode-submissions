from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS
        # run a bfs when we find a 

        rows = len(grid)
        cols = len(grid[0])

        def bfs(starting_row, starting_col):
            area = 1
            queue = deque()
            visited = set()
            visited.add((starting_row, starting_col))
            queue.append((starting_row, starting_col))
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    curr_row, curr_col = queue.popleft()
                    grid[curr_row][curr_col] = 0
                    for neighbor in get_neighbors(curr_row, curr_col):
                        if neighbor not in visited:
                            area += 1
                            visited.add(neighbor)
                            queue.append(neighbor)
            return area

        def get_neighbors(row, col):
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            neighbors = []
            for dr, dc in directions:
                cr, cc = row + dr, col + dc
                if cr >= 0 and cr < rows and cc >= 0 and cc < cols:
                    if grid[cr][cc] == 1:
                        neighbors.append((cr, cc))
            return neighbors

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(bfs(row, col), max_area)
        return max_area