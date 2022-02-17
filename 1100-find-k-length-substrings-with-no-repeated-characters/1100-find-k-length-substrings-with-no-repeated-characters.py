class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26:                 # as for k > 26, there can be no substrings 
            return 0                # with only unique characters
        answer = 0
        n = len(s)
        
        left = right = 0
        
        freq = [0] * 26
        
        def get_val(ch):
            """obtains the index of a character according to the alphabet"""
            return ord(ch) - ord("a")
        
        while right < n:
            freq[get_val(s[right])] += 1  # Add the current ch in the freq array
            while freq[get_val(s[right])] > 1: # If the curr ch appears > 1
                freq[get_val(s[left])] -= 1 # contract the window and remove ch
                left +=1  # till the frequency of the current character becomes 1
            if right - left +1 == k: # check if len(substring)== k
                answer += 1
                freq[get_val(s[left])] -= 1 # Contract window & remove the left ch
                left += 1
            right += 1   # Expand the window
            
        return answer
        # Time complexity: O(n).
        # Space complexity: O(m) = O(26) = O(1)