class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        source_len, target_len = len(s), len(t)

        # the source string is empty
        if source_len == 0:
            return True

        # matrix to store the history of matches/deletions
        dp = [ [0] * (target_len + 1) for _ in range(source_len + 1)]

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, target_len + 1):
            for row in range(1, source_len + 1):
                if s[row - 1] == t[col - 1]:
                    # find another match
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from previous prefixes
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

            # check if we can consume the entire source string,
            #   with the current prefix of the target string.
            if dp[source_len][col] == source_len:
                return True

        return False
    
    # Time Complexity: O(∣S∣⋅∣T∣)
    # Space complexity =  O(∣S∣⋅∣T∣)
        
                    
        