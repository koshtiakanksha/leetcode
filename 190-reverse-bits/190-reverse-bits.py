class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        res = 0
        while n:
            res += ((n%2)*2)**power
            n = n >> 1
            power = power -1
        return res
        