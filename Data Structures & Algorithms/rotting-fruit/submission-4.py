from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # return minimum number of minutes until there is no fresh fruit
        # if its impossible return -1

        # loop through the grid until i find a rotten fruit
            # start a BFS from the rotten fruit
            # start minute tracker
            # get_neighbors function -> return neighbors that are fresh
            # Loop through neighbors


        # after I do the BFS I need to check the original grid to see if there is fresh fruit
        # I can loop through that grid, and check for fresh fruit
            # If I find it, i return -1
            # If not return minutes


        rows = len(grid)
        cols = len(grid[0])

        # grid = [[1,1,0],[0,1,1],[0,1,2]]
        # 

        def Bfs(starting_queue):
            queue = deque()
            visited = set()
            for i in range(len(starting_queue)):
                queue.append(starting_queue[i])
                visited.add(starting_queue[i])
            mins = 0
            while queue:
                level_size = len(queue)
                if_rotted = False
                for _ in range(level_size):
                    cr, cc, = queue.popleft() # get the current row and col from queue
                    for nr, nc in get_neighbors(cr, cc):
                        if (nr, nc) not in visited:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            if_rotted = True
                if if_rotted == True:
                    mins += 1
            return mins


        def get_neighbors(cr, cc):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            neighbors = []
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: #If its in bounds and a fresh fruit
                    neighbors.append((nr, nc))
            return neighbors
            

        starting_queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    starting_queue.append((i, j))
        mins = Bfs(starting_queue)
        print(mins)
        print(grid)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return mins
    
        