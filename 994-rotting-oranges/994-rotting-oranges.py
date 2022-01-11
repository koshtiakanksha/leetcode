class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        q.append((-1, -1))

        time = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col = q.popleft()
            if row == -1:
                time += 1
                if q:  
                    q.append((-1, -1))
            else:
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if ROWS > r >= 0 and COLS > c >= 0:
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            fresh -= 1
                            q.append((r, c))
        return time if fresh == 0 else -1