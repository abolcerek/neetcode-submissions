from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS
        #search for 1's in the grid
        # if there is a 1 start bfs from that point and set the 1's to 0's
        #increment island counter and continue search
        rows = len(grid)
        cols = len(grid[0])

        def BFS(starting_row, starting_col):
            visited = set()
            queue = deque()
            queue.append((starting_row, starting_col))
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    curr_row, curr_col = queue.popleft()
                    grid[curr_row][curr_col] = "0"
                    for neighbor in get_neighbors(curr_row, curr_col):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

        def get_neighbors(row, col):
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if grid[nr][nc] == "1":
                        neighbors.append((nr, nc))
            return neighbors

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    BFS(row, col)
                    islands += 1
        return islands