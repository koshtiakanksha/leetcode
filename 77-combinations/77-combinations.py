class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first, curr):
            """ create another function inside a function with parameters first, which is the value we are curently at and curr is the combination we have. """
            if len(curr)== k:               # when we get the desired length of combination
                res.append(curr.copy())    # append the copy of current combination to the res
            for i in range(first, n+1):     # since the last value is non-inclusive
                curr.append(i)             # append i to the curr combination
                backtrack(i+1, curr)       # call the function for next combination
                curr.pop()                 # to pop the most recent combination
        backtrack(1, [])        # we start from 1, and combination at start is an empty list
        return res     
        
        