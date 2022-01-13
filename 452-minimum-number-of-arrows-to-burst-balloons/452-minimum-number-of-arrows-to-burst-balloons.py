class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0               # if it is an empty list, we return zero
        points.sort(key =lambda x : x[1])             # sort the list in increasing order
        
        arrows = 1                 # since the list is non-empty, atleast 1 arrow is required
        prev_end = points[0][1]      # set prev_end to the second ele of the first ele of list
        for start, end in points:      # iterate through every list in a list
            if prev_end < start:   # if the end of previous list < start of the curr list
                arrows += 1         # we add one to arrow
                prev_end = end          # set prev_end to the current end
        return arrows
   
 # Time complexity : O(NlogN) because of sorting of input data.
    # Space complexity : O(N)

    
    
            
        