class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals]) # we are creating two sorted lists of start
        end = sorted([i[1] for i in intervals])   # and end points, separately
            
        res, count = 0, 0                       # count = no. of meeting rooms right now, 
                                                # res = max no. of rooms used in any interval
        s, e = 0, 0                             # setting the pointers for while loop
        
        while s < len(intervals):           # till we reach the last element in list of start
            if start[s] < end[e]:         # we add one to the count since metting has already 
                count += 1                        # started before the previous meeting ends.
                s += 1                       # also, we update our s pointer
                
            else:                            # We decrement one from the count, 
                count -=1                    # since no meetings are overlapping
                e +=1                        # also, we update the e pointer
            res = max(res, count)    # we store max no. of rooms used in any interval in res.
        return res
    
    # Time Complexity: O(NlogN) 
    # Space Complexity: O(N)
            
        