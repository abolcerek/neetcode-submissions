from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def BFS(starting_node):
            queue = deque()
            visited = set()
            queue.append(starting_node)
            visited.add(starting_node)
            grid[starting_node[0]][starting_node[1]] = "0"
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    curr = queue.popleft()
                    for nr, nc in get_neighbors(curr):
                        if (nr, nc) not in visited:
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
                            visited.add((nr, nc))


        def get_neighbors(curr):
            cr = curr[0]
            cc = curr[1]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    neighbors.append((nr, nc))
            return neighbors



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    BFS((i, j))
                    islands += 1
        return islands