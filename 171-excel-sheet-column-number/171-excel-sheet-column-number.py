class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabets = "0abcdefghijklmnopqrstuvwxyz"
        result = 0
        for i in range(len(columnTitle)):
            result = result * 26
            result += alphabets.index(columnTitle[i].lower()) 
        return result
    
    # time complexity = O(N)
    # space complexity = O(1)