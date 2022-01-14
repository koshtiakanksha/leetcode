class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] *(len(triangle)+1)     # to create a list of len = length of triangle +1
        for row in triangle[::-1]:                      # reversing the triangle
            for i, n in enumerate(row):             # n is the value that comes after looping,
                dp[i] = n + min(dp[i], dp[i+1])      # add it to the min of both
        return dp[0]                             # return the zeroth element in the list

    # time complexity = O(n^2)
    # space complexity = O(n)