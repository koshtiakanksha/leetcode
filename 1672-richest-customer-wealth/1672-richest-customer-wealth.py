class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in accounts:
            maximum = max(maximum, sum(i))
        return maximum
        