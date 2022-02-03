class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount+1)              # create an array of len(amount+1)
        dp[0] = 0                                 # initiate first index to 0
        for a in range(1, amount + 1):           
            for c in coins:
                if (a-c)>= 0:           # subtraction should be positive
                    dp[a] = min(dp[a], 1+dp[a-c])    # update the dp
        if dp[amount] != amount+1:           # the coins can make the amount
            return dp[amount]     # return the number of coins
        else:              
            return -1
        
        # time complexity = O(Amount*number of coins)
        # space complexity = O(Amount)