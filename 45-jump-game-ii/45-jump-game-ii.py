class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0        # initially we set jump to 0
        l = 0            # left and right pointers are set to 0
        r = 0
        while r < len(nums)- 1:   # till r pointer isn't equal to the index of last val
            farthest = 0     # create a new var to store the farthest dist it can cover
            for i in range(l, r+1):  # since the end value isn't inclusive, add 1 to r
                farthest = max(farthest, i+nums[i])  # current index + max jump at i
            l = r+1       # update our variables
            r = farthest   
            jump += 1       # increment our jump by 1
        return jump     
    
    # time complexity = O(N)
    # space complexity = O(1)
        