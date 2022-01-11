class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
                
        dp = [[math.inf if mat[i][j] != 0 else 0 for j in range(cols)] for i in range(rows)]
                    
        for i in range(rows):
            for j in range(cols):
                if i> 0:
                    dp[i][j] = min(dp[i][j], 1+dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], 1+dp[i][j-1])
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i < rows-1:
                    dp[i][j] = min(dp[i][j], 1+dp[i+1][j])
                if j < cols-1:
                    dp[i][j] = min(dp[i][j], 1+dp[i][j+1])
        return dp
                    
                    
                    
            
                