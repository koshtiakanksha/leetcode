class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]                # where we are adding all are subsets to
        nums.sort()
        def backtrack(i, subset): # i-index in nums; subset - current subset;
            if i == len(nums):
                res.append(subset[::]) # to make a copy to avoid going through it twice
                return       # we dont want to keep backtracking, once we reach the end
            
            # all subsets that include nums[i]
            
            subset.append(nums[i]) 
            backtrack(i+1, subset)
            subset.pop() # remove value from the subset that we just added
            
            # all subsets that do not include nums[i]
            
            while i+1< len(nums) and nums[i]== nums[i+1]: # [1,2,2] we skip second 2, to                                                                avoid repetition
                i += 1
            backtrack(i+1, subset)
        backtrack(0, [])
        return res
    
    # time complexity = O(n2^n)
    # space complexity = O(n2^n)
            
                