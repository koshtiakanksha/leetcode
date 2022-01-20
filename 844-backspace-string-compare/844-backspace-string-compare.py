class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_t=[]      # we create two empty lists to store the new str after using backspaces
        res_s=[]
        
        for i in s:          # iterate through every character in a string
            if i != "#":           # if it is a letter we append it to our list
                res_s.append(i)
            else:            # if it is a "#" 
                if res_s:           # and if the new list is not None
                    res_s.pop()      # we remove the last added character from the list
        
        for i in t:                    # we do the same for "t" string
            if i != "#":
                res_t.append(i)
            else:
                if res_t:
                    res_t.pop()
                    
        return res_s == res_t     # if both the lists are equal, we return True
    
    # time complexity = O(M+N)
    # space complexity = O(M+N)
    