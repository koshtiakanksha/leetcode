class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]                         # we assume the minimum to be at the index zero
        l, r = 0, len(nums)-1                 # set var l and to 0 and length of the array
        while l <= r:                       # since we dont want to go through any ele twice
            if nums[l] < nums[r]:             # if the element at index l is less than right
                res = min(res, nums[l])       # we set our res to the minimum of both
                break                         # we break our code here
            m = (l+r)// 2                     # we set our middle pointer, (sum of l and r)//2 
            res = min(res, nums[m])           # and set our res to the minimum of both
            
            if nums[m] <= nums[r]:        # if the m pointer is less than the element at r 
                r = m-1                   # we set our right pointer to the left of middle
            else:                         # if the m pointer is greater than the element at r
                l = m+1                   # we set our left pointer to the right of middle
        return res
            
        # Time Complexity : O(logN)
        # Space Complexity : O(1)
