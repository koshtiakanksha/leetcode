class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1                     # index val of last element in the list
        for i in range(len(nums)-1,-1,-1):     # we want the list in the reverse order
            if i + nums[i]>= goal:           # if we can reach to this element before the goal
                goal = i                   # it means that we hve to reach to the previous one
        return goal == 0           # because after that we know we can reach the last ele
                                      # so we set our goal to the index of previous one
                                      # at the end if goal == 0, i.e if we reach the first ele
                                      # we return True
    
    
    # time complexity = O(N)
    # space complexity = O(1)
    # approach used = Greedy