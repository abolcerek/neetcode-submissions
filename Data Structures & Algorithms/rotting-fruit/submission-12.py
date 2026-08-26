from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(start):
            queue = deque(start)
            visited = set()
            for row, col in start:
                visited.add((row, col))
            print(f'This is visited: {visited}')
            mins = 0
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    curr_row, curr_col = queue.popleft()
                    for neighbor in get_neighbors(curr_row, curr_col):
                        if neighbor not in visited:
                            grid[neighbor[0]][neighbor[1]] = 2
                            visited.add(neighbor)
                            queue.append(neighbor)
                mins += 1
            return mins

        def get_neighbors(row, col):
            neighbors = []
            for dr, dc in directions:
                cr, cc = row + dr, col + dc
                if 0 <= cr < rows and 0 <= cc < cols:
                    if grid[cr][cc] == 1:
                        neighbors.append((cr, cc))
            return neighbors

        if rows == 1 and cols == 1:
            if grid[0][0] == 1:
                return -1
            else:
                return 0

        start = []
        is_rotten = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    start.append((row, col))
                    is_rotten = True
        if is_rotten != True:
            is_1 = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        is_1 = True
            if is_1:
                return -1
            else:
                return 0


        mins = bfs(start)
        res = mins - 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return res