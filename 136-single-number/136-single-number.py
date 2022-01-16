class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dummy = []                              # create an empty list
        for i in nums:
            if i not in dummy:         # we add i to dummy if i is not already in it
                dummy.append(i)
            else:                      # we remove i if it is in dummy
                dummy.remove(i)
        return dummy.pop()            # we return the one element in the list
        
        
# time complexity: O(n^2)
# space complexity: O(n)
