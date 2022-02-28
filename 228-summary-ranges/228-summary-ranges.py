class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        prev = nums[0]
        curr = nums[0]
        end = None
        res = []
        for i in range(1,len(nums)):
            curr += 1
            if nums[i] == curr:
                end = nums[i]
            else:
                if not end:
                    res.append(str(prev))
                else:
                    res.append(str(prev) + "->" + str(end))
                prev = nums[i]
                curr = nums[i]
                end = None
        if not end:
            res.append(str(prev))
        else:
            res.append(str(prev) + "->" + str(end))
        return res
    
    # time complexity = O(N)
    # space complexity = O(N)
            
                    
                
            
                    
        
                
                
                
                    
        