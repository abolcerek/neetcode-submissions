from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # loop through grid for o
        # then bfs from o and see if the neighbors are o's or not on the edge and not in range
        rows = len(board)
        cols = len(board[0])

        def bfs(row, col):
            queue = deque()
            visited = set()
            queue.append((row, col))
            visited.add((row, col))
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    r, c = queue.popleft()
                    neighbors, res = get_neighbors(r, c)
                    if res == False:
                        return
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            for cr, cc in visited:
                board[cr][cc] = "X"


        def get_neighbors(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols: #if inbounds
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1: #if on edge
                        if board[nr][nc] == "O": #if on edge and O
                            return neighbors, False #return false its not surrounded
                    if board[nr][nc] == "O":
                        neighbors.append((nr, nc))
            return neighbors, True

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == "O":
                    bfs(row, col)