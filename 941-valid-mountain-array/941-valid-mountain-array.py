class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)< 3:
            return False
        if (arr[1] > arr[0]) and (arr[len(arr)-1]<arr[len(arr)-2]):
            i = 0
            while arr[i]< arr[i+1]:
                i+=1
            for j in range(i, len(arr)-1):
                if arr[j]<= arr[j+1]:
                    return False
        else:
            return False
        return True