from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start a BFS from each land cell
        # track how many steps we have taken
        # once we reach a treasure, set the original cell to be the value

        rows = len(grid)
        cols = len(grid[0])

#         # Input: [
#               [2147483647,-1,0,2147483647],
#               [2147483647,2147483647,2147483647,-1],
#               [2147483647,-1,2147483647,-1],
#               [0,-1,2147483647,2147483647]
# ]

        def bfs(starting_node):
            starting_row, starting_col = starting_node[0], starting_node[1]
            queue = deque()
            visited = set()
            queue.append(starting_node)
            visited.add(starting_node)
            steps = 0
            while queue:
                levels = len(queue)
                steps += 1
                for _ in range(levels):
                    r, c = queue.popleft()
                    for nr, nc in get_neighbors(r, c):
                        if (nr, nc) not in visited:
                            if grid[nr][nc] == 0:
                                grid[starting_row][starting_col] = steps
                                return
                            else:
                                queue.append((nr, nc))
                                visited.add((nr, nc))

            


        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for dr, dc in directions: # Only adding to neighbors if it can be traversed or if its a treasure chest
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    neighbors.append((nr, nc))
            return neighbors


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2147483647:
                    bfs((row, col))
    