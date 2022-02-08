class Solution:
    def addDigits(self, num: int) -> int:
        if num < 9:
            return num
            
        while num > 9:
            num = (num % 10) + (num// 10)
        return num
        