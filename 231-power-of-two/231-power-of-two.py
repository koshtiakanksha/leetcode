class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:              # since zero cannot be the power of two, we return False
            return False 
        
    # we are going to convert the given decimal, n, into binary number. (1) 
    # Then we are going to take the compliment of that binary number. Add one to it (2)
    # Then do the & operation on eqn (1) and(2)
    
        return (n & -n == n)
    
    # for example: if n= 6: 0110 
    # complement of 6 + 1 : 1010 =  1001 + 0001
    # using & op on both  : 0010
    
    
    # time complexity= O(1)
    # space complexity = O(1)
        
        