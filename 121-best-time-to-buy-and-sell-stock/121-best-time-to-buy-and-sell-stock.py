class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1        # l pointer to be at 0, right pointer to be at 1 
        maxProfit = 0            # maxProfit = 0, default case
        while r < len(prices):            # to keep r in bounds
            if prices[l] < prices[r]:       # since we do not want the loss
                profit = prices[r] - prices[l]   # calculate the profit
                maxProfit = max(profit, maxProfit)   # update the maxProfit
            else:        # else we update l pointer to be at the position of r
                l = r 
            r += 1      # increment r otside if cases
        return maxProfit   # return the maxProfit
    
    # time complexity = O(N)
    # space complxity = O(1)
                
                
                