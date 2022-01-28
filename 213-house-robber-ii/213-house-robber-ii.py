class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:        # if the len is ess than 3, we return max from the list
            return (max(nums))
        
        def max_rob(start,end):   # we def new function, that takes the start & end index
            res1 = 0                                       #suppose it starts at index 0
            res2 = 0                                       #suppose it starts at index 1
        
            for i in range(start, end):          
                temp = max(res1+nums[i], res2)# we add adj numbers ans store max in temp
                res1 = res2
                res2 = temp       
            return res2      # return the max
        return max(max_rob(0,len(nums)-1), max_rob(1,len(nums)))   # we call the function twice, once, starting with index 0, and the other with index 1 and return the max of both
    
    # time complexity = O(N)
    # space complexity = O(1)