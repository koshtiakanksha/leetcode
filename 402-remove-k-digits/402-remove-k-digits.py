class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numstack = []
        for digit in num:   # create an increasing sequence of digits
            while k and numstack and numstack[-1] > digit:
                numstack.pop()
                k -= 1
            numstack.append(digit)
            
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalstack = numstack[:-k] if k else numstack  
        
        return "".join(finalstack).lstrip('0') or "0" # trip leading zeros
    
    # time complexity = O(N)
    # space complexity = O(N)