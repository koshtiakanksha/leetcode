class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}      # base case, when empty string, we return 1
        
        def dfs(i):  # i is the index
            if i in dp: # already decoded or, len(s), this is base case
                return dp[i]
            if s[i]=="0":    # first letter in a string can't be zero
                return 0
            res = dfs(i+1)  # res is the subproblem, that is dfs(i+1)
            if (i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")): 
                res += dfs(i+2)
            dp[i]= res      # store the value of res in dp[i]
            return res      # return for inside function
        return dfs(0)       # call the function dfs with parameter 0
                
    # time complexity = O(N)
    # space complexity = O(1)