class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1
    
    # time complexity = O(N)
    # space complexity = O(1)
        