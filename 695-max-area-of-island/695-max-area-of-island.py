class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)                       #no of rows
        columns= len(grid[0])                  #no of columns
        visit = set()              #create a set to avoid going to the visited position twice
        
        def dfs(r, c):
            if (r<0 or                         
                r== rows or
                c<0 or                          
                c == columns or             #since all these are out of the grid
                grid[r][c]== 0 or               #since 0 indicate water
                (r,c) in visit):       #since we do not want to go through visited cell twice 
                return 0
            visit.add((r,c))           #need to update the visit set 
            return (1+ dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))   #to find the extended                                                                    area in all four directions
        
        area = 0
        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r,c))   #since we need to find the maximum area
        return area
    
    # time complexity = O(m*n)      (dimensions of the matrix)
    # it is a worst case scenario, if we have to go through each cell
    # space complexity = O(m*n)