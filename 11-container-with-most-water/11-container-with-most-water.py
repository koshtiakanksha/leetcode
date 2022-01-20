class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1          # set the pointers
        water = 0                         # to store the max water, initially set it to zero
        while l < r:                      # we don't want to change the pos of our pointers
            res = (r-l) * min(height[l], height[r])# we create new var and calculate max water
            water = max(water, res)              # to store the max at any given point
            if height[l] > height[r]:    # we move to right if the height of right pointer
                r -= 1                             # is less than that of left
            else:                        # vice versa
                l += 1
        return water                # return the max water, the container can store
        
        