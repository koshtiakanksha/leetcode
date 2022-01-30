class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
            else:
                total += (count +1)*count//2
                count = 0
        total+=(count+1)*count//2
        return total
