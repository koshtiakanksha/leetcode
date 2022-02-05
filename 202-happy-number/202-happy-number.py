class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()     # to keep track of numbers we've visited
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        return False      # it is not a happy number
    
    
    def sumOfSquares(self, n):
        output = 0    #sum of squares' value
        
        while n:
            digit = n%10
            digit = digit**2
            output += digit
            n = n//10
        return output    
        
    # time complexity = O(n)
    # space complexity = O(n)