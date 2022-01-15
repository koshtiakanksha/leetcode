class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0          # to save the one bits. initially set it to zero
        while n:         # run the loop till n exists
            res += n%2   # to add one, we use mod of 2 on n
            n = n >> 1   # shift n by 1 position to the right
        return res         
    
    # time complexity: O(32) since it is given that the input is a binary string of bit 32
    