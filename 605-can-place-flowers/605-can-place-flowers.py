class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]       # we create a new list and add zeros to start and end 
        for i in range(1, len(f)-1):                
            if f[i-1] == 0 and f[i]== 0 and f[i+1]== 0:    # if three consecutive zeros
                f[i] = 1                              # we replace the middle zero by one
                n -= 1                        # we decrease one from n 
        return n <= 0               # if n is less than or equal to zero, we return True
          
        # Time complexity = O(n)
        # space complexity = O(1)