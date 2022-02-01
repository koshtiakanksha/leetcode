class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}             # key = index, value = [ lenLIS, count of LIS]
        lenLIS, res = 0, 0    # lenLIS, count of LIS
        
        # i is the start of subseq
        for i in range(len(nums)-1, -1, -1): # iterate through i in reverse order
            maxLen, maxCount = 1, 1   # length, count of LIS from index i
            for j in range(i+1, len(nums)):  # j >= i+1, j< len(nums)
                if nums[j]> nums[i]:  # make sure it is in increasing order
                    length, count = dp[j]   # len, cnt of LIS starting from index j 
                    if length + 1 > maxLen:
                        maxLen, maxCount = length +1, count
                    elif length + 1 == maxLen:
                        maxCount += count
            if maxLen > lenLIS:      # update global variables
                lenLIS, res = maxLen, maxCount
            elif maxLen== lenLIS:
                res += maxCount
            dp[i]= [maxLen, maxCount]    # update dp
        return res  # return the max count of LIS
    
    # time complexity = O(N**2)
    # space complexity = O(N**2)
            
            
        
        