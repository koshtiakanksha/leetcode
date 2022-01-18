class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1                # we set l, r pointer to 0 and the last index
        while l < r:                         # since we dont want to go through 1 ele twice
            mid = (l+r)// 2                  # we set our middle pointer as (l+r)//2
            if nums[mid] > nums[mid + 1]:    # peak ele is greater than neighbors and since 
                r = mid                      # the middle is greater, we set our r to mid
            else:                          
                l = mid + 1            # else we set l to mid + 1
        return l 
    
    # Time complexity : O(log_2(n))
    # Space complexity : O(1)