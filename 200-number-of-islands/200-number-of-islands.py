class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        res = 0
        
        if not grid:
            return 0
        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col= q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r, c= row+dr, col+dc
                    if (r in range(rows) and
                        c in range(columns) and
                        grid[r][c]=="1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    res += 1
        return res
        
        