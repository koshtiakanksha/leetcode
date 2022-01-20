class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1                          # we initialize our left pointer to 1
        right = max(piles) # right pointer to max(piles), since she goes thru 1pile in 1 hour
        res = right      # and we set our res to the maximum value, result cannot excede this
        while left<=right:          # we don't want to change the positions of left and right
            k = (left+right)//2      # middle element
            hours = 0                     # initially set hours to zero
            for i in piles:                 # iterate through the piles
                hours += math.ceil(i/k)      # we round off i/k and add it to hours
            if hours <= h:                   # if our hour is less than we move to left
                res = min(res, k)          # set our res to min of both
                right = k -1 
            else:                            # if it is more, than we move to the right
                left = k+1
        return res
    
   # time complexity= O(log(max(p))*p)
   # space complexity = O(1)