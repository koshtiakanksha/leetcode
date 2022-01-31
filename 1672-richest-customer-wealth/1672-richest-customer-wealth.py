class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0                         # initiate to 0, to store the maximum
        for i in accounts:                  # iterate through every list in accounts
            maximum = max(maximum, sum(i))  # update the max variable to the max amount
        return maximum                      # return the max amount
    # time complexity = O(N)
    # space complexity = O(1)
        