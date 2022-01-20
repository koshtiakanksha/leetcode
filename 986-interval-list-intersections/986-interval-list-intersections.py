class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []                 # create an empty list to store our values of intersections
        i= 0                     # set i pointer to 0
        j = 0                    # set j pointer to 0
        while i < len(firstList) and j< len(secondList):  # till the end of the list
            start = max(firstList[i][0], secondList[j][0])  # the starting point of the range
            end = min(firstList[i][1], secondList[j][1])    # the end point of the range
            
            if start <= end:                   # start should be <= end to append the values
                res.append([start, end])
                
            if firstList[i][1] < secondList[j][1]:  # if end of first is less than end of sec
                i += 1     # we add one to i. i.e check the neck of 1st with same of 2nd list
            else:                            # and vice versa
                j += 1
        return res                
        
        
        # time complexity = O(M+N)
        # space complexity = O(M+N)