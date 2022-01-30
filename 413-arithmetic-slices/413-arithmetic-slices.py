class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in range(2, len(nums)): # iterate through every number
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:  # check 3 adj nums
                count += 1                     # we increment count by 1
            else:                            # if the chain is broken
                total += (count +1)*count//2 # we add the formula to count
                count = 0                     # we set the count to zero
        total+=(count+1)*count//2    # we add the formula to count         
        return total
    
    # time complexity = O(N)
    # space complexity = O(1)
    
    
