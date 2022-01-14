class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp= one                 # we need to create a new var to save the value of one
            one= one + two           # since this is the updated value of one
            two = temp              # and we need to set var two equals to the previous value                                               of one, i.e. temp
            
        return one
    
        # time complexity = O(n)
        # space complexity = O(n)