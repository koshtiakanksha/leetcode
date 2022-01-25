class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)< 3:    # if length of array is less than 3 we return False
            return False
        # first, we'll check if one and last values are lowest
        if (arr[1] > arr[0]) and (arr[len(arr)-1]<arr[len(arr)-2]):
            i = 0
            while arr[i]< arr[i+1]:    # store the value of i till its heighest, peak
                i+=1
            for j in range(i, len(arr)-1):   # after peak, if the value doesn't decrease 
                if arr[j]<= arr[j+1]:         # we return false
                    return False
        else:                       # if first and last aren't lowest
            return False
        return True
    
    # time complexity: O(n)
    # space complexity: O(n)