class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()    # to make sure that we don't revisit the same position twice
        
        def dfs(r,c, i):    # nested function with arg of current position, i= target
            if i == len(word):   # that is when we find our answer
                return True
            if (r<0 or c< 0 or    
                r>=rows or c>= cols or    # if r and c out of bounds
                word[i] != board[r][c] or   # if it is not the letter we are looking for
                (r,c) in path):  # if we have already visited this set
                return False
            path.add((r, c))   # since it is what we want, we add it to our path
            res = (dfs(r+1, c, i+1)or
                  dfs(r-1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r, c-1, i+1))   # we look for the next letter in all 4 directions
            path.remove((r,c))   # we don't want to continue to visit the same position
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True     # can return True multiple times
        return False    # if in above lie it returns false once, then it stops and return False
                
            
        # time complexity = O(n*m*4^len(word))
        # space complexity = O(m*n)
        