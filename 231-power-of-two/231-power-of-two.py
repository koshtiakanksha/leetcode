class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:              # since zero cannot be the power of two, we return False
            return False
        while n % 2 == 0: # we stop once the val != 0, because then it can't be the power of 2
            n = n / 2      # we update the value of n to avoid endless loop
        return n == 1       # return true if, in the end/ outside the while loop, n==1
    
    # time complexity= O(logN)
        
        