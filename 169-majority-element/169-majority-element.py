class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        return candidate
    
    # time complexity = O(n)
    # space complexity = O(1)
        