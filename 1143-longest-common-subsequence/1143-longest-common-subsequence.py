class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
                                                        # create a matrix of m * n
        for i in range(len(text1)-1, -1, -1):    # iterate through t1 in reverse order
            for j in range(len(text2)-1, -1, -1):# iterate through t2 in reverse order
                if text1[i]== text2[j]:    # if both are same
                    dp[i][j] = 1 + dp[i+1][j+1]# we add 1 to the diagonal and set to dp
                else:                            # if both aren't same
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])   # take max of right & down
        return dp[0][0]
    
    # time complexity = O(m*n)
    # space complexity = O(m*n)