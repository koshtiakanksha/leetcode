class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0          # to save the one bits. initially set it to zero
        while n:         # run the loop till n exists
            n = n & (n-1)
            res += 1
        return res
            
    # consider n =  01011
    # now n - 1  =  01010
    # use & op   =  01010, set it equal to n
    # add one to the result after every loop
    # do this till we get n = 00000
            
    # time complexity: O(32) since it is given that the input is a binary string of bit 32
    