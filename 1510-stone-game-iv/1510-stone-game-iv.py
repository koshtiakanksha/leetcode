class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if dp[i-k*k] == False:
                    dp[i] = True
                    break
        return dp[n]
    
       # Time complexity: (O(N\sqrt{N}))
       # space complexity : O(N)
   
    # example testcase, n=4
    # dp = [False, False, False, False, False]
    
    # (i,k)=(1, 1), i = 1, i-k*k = 0, dp[0]=False -> dp[1]=True
    # (i,k)=(2, 1), i = 2, i-k*k = 1, dp[1]=True
    # (i,k)=(3, 1), i = 3, i-k*k = 2, dp[2]=False -> dp[3]=True
    # (i,k)=(4, 1), i = 4, i-k*k = 3, dp[3]=True
    # (i,k)=(4, 2), i = 4, i-k*k = 0, dp[0]=False -> dp[4]=True
    
    # dp = [False, True, False, True, True]
    # dp[n] = dp[4] = True

    