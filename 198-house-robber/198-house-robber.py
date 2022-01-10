class Solution:
    def rob(self, nums: List[int]) -> int:
        res1 = 0                                           #suppose it starts at index 0
        res2 = 0                                           #suppose it starts at index 1
        
        # [res1, res2, i, 1+1,.....]
        
        for i in nums:
            temp = max(res1+i, res2)             # assuming res2 to be adjacent to i
            res1 = res2                          # moving to the right
            res2 = temp                          # since temp has the maximum value
        return res2                              # res2 will return the maximum amount
            
        
        