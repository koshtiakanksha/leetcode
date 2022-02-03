class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        
        def dfs(nums):
            if nums in dp:
                return dp[nums]
            dp[nums] = 0 if nums==n else nums
            for i in range(1, nums):
                val = dfs(i)*dfs(nums-i)
                dp[nums] = max(dp[nums], val)
            return dp[nums]
        return dfs(n)
    
    # time complexity = O(n**2)
    # space complexity = O(n)