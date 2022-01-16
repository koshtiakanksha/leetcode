class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0                  # initially we set a equals to 0
        for i in nums:         # then we iterate through every element in the list
            a = a ^ i          # then we XOR a with i to find the unique number.
        return a               # return the unique number
    
    
    # XOR: XOR all bits together to find the unique number.

# XOR : a (XOR) 0 = a, a (XOR) a = 0
# nums = [2,2,1] -> 0 (XOR) 2 = 2, 2 (XOR) 2 = 0, 0 (XOR) 1 = 1
    
        
# time complexity: O(n)
# space complexity: O(1)
