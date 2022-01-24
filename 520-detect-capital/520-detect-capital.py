class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # if length of word is 1, we do not care if it is lower or upper
        
        if len(word)== 1:
            return True
        
        # if letters at index 0 and index 1 are upper, then we check if the rest are upper, if not, we return False
        
        if word[0].isupper() and word[1].isupper():
            for i in range(2,len(word)):
                if not word[i].isupper():
                    return False
        
        # for second and third case, we do not care if the first letter is upper or lower. The else case here mean that the letter at index 1 is not upper(lower). So, we want the rest of letters to be lower. and if not we return False
        
        else:
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True           # if any one of the cases, returns True
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
                
            
        
        