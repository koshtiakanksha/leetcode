class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch = 0       #Initialize a variable ch which would hold the XORed results.
        for char in s:  # XOR all the characters with ch while iterating through s
            ch ^= ord(char)
        for char in t:    # similar to t
            ch ^= ord(char)
        return chr(ch)   # Return ch as the answer
    
    # time complexity = O(N)
    # space complexity = O(1)