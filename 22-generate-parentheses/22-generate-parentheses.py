class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if open< n
        # only add closing parentheses if closed < open
        # valid iff open == closed==n
        stack = []                 # to hold our parentheses
        res = []              # to store all the valid parenthesis
        def backtracking(o,c):   # recurcive
            if o==c==n:                # base case
                res.append("".join(stack))   # convert it to str and append to res
                return               # return since it is base case
            if o < n:
                stack.append("(")   # we add one to o in our backtracking function since
                backtracking(o+1, c)    # we've added one open parentheses to stack
                stack.pop()            # we update the stack, since we only have one stack var
            if o > c:                       
                stack.append(")")     # repeat the same for closing parentheses
                backtracking(o, c+1)
                stack.pop()
        backtracking(0,0)  # since initial values of open and closed are 0
        return res
            
        
        # time complexity:O((4^n)/(n^(1/2))) 
        # space complexity: O((4^n)/(n^(1/2))) 