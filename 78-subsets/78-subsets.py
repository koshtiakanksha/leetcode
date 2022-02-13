class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]             # create a list that contains one empty list
        for num in nums:         # iterate through nums
            output += [curr + [num] for curr in output]   # we add one value from the nums b                                                         list to every element in the output list
        
        return output
        
        # time complexity: O(N*2^N)
        # space complexity: O(N*2^N)        