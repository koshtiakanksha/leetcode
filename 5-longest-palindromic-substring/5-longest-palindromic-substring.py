class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""                # default case
        reslen = 0              
        for i in range(len(s)):
            l, r = i, i      # for odd length palindrome
            while l >= 0 and r< len(s) and s[l] == s[r]: # 1st loop, the same letter
                if (r-l+1)> reslen:           # since we want the longest substring
                    res = s[l:r+1]            # we save the string
                    reslen = r-l +1              # update the length of largest str 
                l -= 1                         # move to left
                r += 1                          # move to right
            l, r = i, i + 1                # for even length
            while l >= 0 and r < len(s) and s[l] == s[r]:  # two adj strings are equal
                if (r-l+1)> reslen:         # since we want the longest substring
                    res = s[l:r+1]          # we save the string
                    reslen = r-l +1         # update the length of largest str 
                l -= 1                      # move to left
                r += 1                       # move to right
        return res
        
# time complexity = O(N**2)
# space complexity = O(1)
        
        
        