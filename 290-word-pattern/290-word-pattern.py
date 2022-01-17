class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char, hashmap = {}, {} # we create two empty hashmaps, one for pattern & one for word
        words = s.split()                     # split the string to separate the words
        if len(words)!= len(pattern):      # if lengths are diff we immediately return False 
            return False
        for c, w in zip(pattern, words):    # we connect two lists and then iterate
            if c not in char:                # if c is not in map, but w is there, it means 
                if w in hashmap:               # it is not following the pattern.
                    return False
                else:
                    char[c] = w              # else we assign their values to w and c resp
                    hashmap[w] = c
            else:
                if char[c] != w:      # and if c is in char it is not equal, we return False
                    return False
        return True                    # if it follows the pattern, we return True
    
    
    # time complexity = O(n)
    # space complexity = O(1)

    
        