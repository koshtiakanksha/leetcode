class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1]*len(nums)        # create a new array of length of nums
        for i in range(len(nums)-1, -1, -1):    # iterate through it in reverese
            for j in range(i+1, len(nums)):     # j should be > i but j < len(nums)
                if nums[j]> nums[i]:    # if ele at jth index > ele at ith index
                    res[i] = max(res[i], 1+res[j]) # update the ith index of res to max
        return max(res)     # return the maximum value in the array
    
    # time complexity = O(N**2)
    # space complexity = O(N)
    
        
        