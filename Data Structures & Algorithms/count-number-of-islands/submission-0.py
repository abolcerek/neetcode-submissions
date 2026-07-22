class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: #if nothing in the grid
            return 0

        islands = 0 #int varable for the islands
        visit = set() #defining set that will be used to mark where land has been visited
        row, col = len(grid), len(grid[0]) #defining rows and colums (the position in the grid)

        def dfs(r, c):
            if (r not in range(row) or c not in range(col) or grid[r][c] == "0" or (r,c) in visit): #if the position if out of bounds or it is water or it has been visited
                return #we return nothing
            visit.add((r,c)) #we add the position to the visit set to mark that the position has now been visited
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]] #all the directions possible to move in
            for dr, dc in directions: #for each direction in the list of directions
                dfs(r + dr, c + dc) #we run a dfs on each direction from the position

        
        for r in range(row): 
            for c in range(col): #for every position in the grid
                if grid[r][c] == "1" and (r,c) not in visit: #if the position is land and has not been visited
                    islands += 1 #we add it to the count of islands
                    dfs(r,c) #we run a dfs on the position

        return islands #we return islands which has the number of islands in it



