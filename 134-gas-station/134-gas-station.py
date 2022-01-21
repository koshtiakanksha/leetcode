class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0       # total is the sum of all gas and costs in the list after iteration
        curr = 0            # curr is the gas at that given point
        start = 0                # we start at index at 0
        for i in range(len(gas)):         # iterate through both the list 
            curr += gas[i] - cost[i]       # we add the gass and subtract the cost from curr
            total += gas[i] - cost[i]           # add the same amount of gas to our total
            if curr < 0:           # if curr is less than zero
                start = i + 1          # we add one to our start
                curr = 0            # and set curr back to zero
        if total >= 0:        # we total is >= o0 i.e. the desired outcome
            return start      # we return the value of start
        else:                 # else we simply return -1, because the solution does't exists
            return -1
                
  # on line 7, we cannot add the curr amount to out total, since we equal it to zero only if its value is less than zero          
            # time complexity = O(n)
            # space complexity = O(1)
        
        