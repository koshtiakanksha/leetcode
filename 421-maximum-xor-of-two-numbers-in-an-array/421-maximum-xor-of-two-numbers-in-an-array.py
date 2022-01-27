class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2           # because by default python adds "0b" as prefix 
        max_xor = 0                          # we set is first to zero
        for i in range(L)[::-1]:               # we want the range in reverse order
            max_xor <<= 1                      # go to the next bit by the left shifter
            curr_xor = max_xor | 1             # set 1 in the smallest bit
            prefixes = {num >> i for num in nums}    # Update max_xor
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)# Checkif p1^p2==curr_xor
        return max_xor
        
    # time complexity = O(N)
    # space complexity = O(1)