class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)     # since it may go out of bounds
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        
        
        reverse(0,len(nums)-1)    # to reverse the whole array
        reverse(0, k-1)           # reverse only the part till the kth index
        reverse(k, len(nums)-1)   # reverse only the part after the kth index
        
       
        
       
        
       
            
        # time complexity = O(n)
        # space complexity = O(1)