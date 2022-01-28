class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0   # we return 0 immediately as it won't make the answer
        prod = 1        # initially we set to 1, and not to 0, because 0 times num is 0
        ans = left = 0     # ans is our end res and left is the pointer starting at 0
        for right, val in enumerate(nums):# right pointer starts at 0 & val = nums[r]
            prod *= val   # after every loop we multiply one val
            while prod >= k:   
                prod /= nums[left]
                left += 1     # since we use div function we increment l by 1
            ans += right - left + 1 
        return ans
      # Time Complexity: O(N)
      # Space Complexity: O(1)
        