class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                                  # we return the output as the list of list 
        nums.sort()                               # we sort the input list
        for i, a in enumerate(nums):              # i is the index and a is the value
            if i > 0 and a == nums[i-1]:          # we dont want to use the same value twice
                continue                          # so we continue
            l, r = i+1, len(nums)-1               # we'll have two pinters left and right
            while l< r:                           # left and right can't be equal
                threesum = a + nums[l] + nums[r]  # since we want the list of three elements
                if threesum > 0:                  # if the sum is greater than zero
                    r -= 1                        # we decrement our right pointer
                elif threesum < 0:                # if the sum is less than zero
                    l += 1                        # we increment our left ponter by one
                else:                             # if ihe sum is equal to zero
                    res.append([a, nums[l], nums[r]]) # we append the list to the res
                    l += 1                              # and increment our left pointer 
                    while nums[l] == nums[l-1] and l<r:  # we skip if the values are repeated
                        l +=1                            
        return res
                
        # time complexity = O(n^2)
        # space complexity = O(1)