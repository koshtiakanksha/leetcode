class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return (max(nums))
        
        def max_rob(start,end):
            res1 = 0                                       #suppose it starts at index 0
            res2 = 0            #suppose it starts at index 1
        
            for i in range(start, end):
                temp = max(res1+nums[i], res2)
                res1 = res2
                res2 = temp
            return res2
        return max(max_rob(0,len(nums)-1), max_rob(1,len(nums)))