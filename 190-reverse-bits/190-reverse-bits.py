class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31                              # the input is a binary string of length 32
        res = 0                                # initially set it to zero
        while n:                                  
            res += ((n%2)*2)**power    # we take the mod of n, then multiply it by 2 and take                                              its power and add it to our res 
            n = n >> 1                     # shift the integer by 1
            power = power -1               # we decrement the power by 1 
        return res
        
        
# time complexity = O(1), since the integer is of fixed size
# space complexity = O(1), since the consumption of memory is constant