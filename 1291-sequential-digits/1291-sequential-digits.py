class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"      # create a string that contain digits from 1 to 9
        res = []                 # empty list to sore all such numbers
        nl = len(str(low))       # as we cannot find the len of int we convert it to str
        nh = len(str(high))      # find lengths of low and high integers
        
        for i in range(nl, nh + 1):    # we want the length of our number to be betw nl & nh+1
            for j in range(0, 10 - i):    # we decrement the length of number from upper bound
                num = int(nums[j: j + i])   # select the desired section and convert it to int
                if num >= low and num <= high: # we want our numbers to fall bet low & high
                    res.append(num)       # we append our number to the res
        return res                        # and then return our res
        
        
        # time complexity = O(1)
        # space complexity = O(1)