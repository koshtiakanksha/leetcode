class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.binarySearch(nums, target, True)    # we call our below functions twice 
        right = self.binarySearch(nums, target, False)   # for first and last position
        return [left, right]
    
    def binarySearch(self, nums, target, leftbias):
        """We put another parameter leftbias, which takes boolean values, True or False, for first and last position resp """
        l = 0                                # we place our left pointer at zero index
        r = len(nums)- 1                     # and right pointer at the last index
        i = -1                        # if we dont find the target, we set our default to -1
        while l <= r:                 # we dont want to go through the list twice
            m = (l+r)//2                # set our middle pointer as m
            if target > nums[m]:        # if our target is greater than the middle value
                l = m + 1            # we skip the remaining values and set l pointer to m+1
            elif target< nums[m]:      # if our target is less than the middle value
                r = m-1               # we skip the remaining values and set r pointer to m-1
            else:                    # if the middle value is equal to target value
                i = m                 # we set i equal to index m
                if leftbias:          # if left bias is true, we search to the left of m
                    r = m-1
                else:                 # if left bias is false, we search to the right of m
                    l = m+1
        return i                       # at the end we return i
        