class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        
        fresh = 0              # we need to run the code until fresh turns back to 0 again
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:     # since they are rotten, add them to deque-. q
                    q.append((r, c))
                elif grid[r][c] == 1:      # add one to the fresh if we find one fresh orange
                    fresh += 1

        q.append((-1, -1))              # to mark the round

        time = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]       # in four directions
        while q:
            row, col = q.popleft()     # since we are using bfs to find the solution
            if row == -1:
                time += 1                             # after one round
                if q:  
                    q.append((-1, -1))                # to avoid endless loop
            else:
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ROWS > r >= 0 and COLS > c >= 0:    # to check the bound
                        if grid[r][c] == 1:
                            grid[r][c] = 2                 # change to rotten
                            fresh -= 1                    # decrease the no. of fresh oranges
                            q.append((r, c))           # add to the deque
        return time if fresh == 0 else -1            