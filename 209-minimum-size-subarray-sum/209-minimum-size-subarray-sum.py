class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0                                # we set our i, initially to zero
        res = len(nums) + 1              # we set our res to len(nums) + 1, for calculations
        for j in range(0, len(nums)):      # we iterate through the list
            target -= nums[j]              # we delete the value of jth index from target
            while(target <= 0):            # while target is <= 0, we continue the loop
                res = min(res, j - i + 1)    # we add one to diff since index starts from 0
                target += nums[i]            # we add the value at ith index to the target
                i += 1                       # increment i by 1
        return res % (len(nums) + 1)      
    # time complexity = O(n)
    # space complexity = O(1)
                 