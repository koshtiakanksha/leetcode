class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower = self.findBound(nums, target, True)
        if (lower == -1):
            return [-1, -1]
        
        upper = self.findBound(nums, target, False)
        
        return [lower, upper]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        start, end = 0, N - 1
        while start <= end:
            mid = int((start + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    start = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
        