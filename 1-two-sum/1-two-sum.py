class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}                              #create an empty dictionary
        for i, n in enumerate(nums):              #iterate through each element in nums
            diff = target - n                #target = n1+n2 -> n1= target-n2 -> n1=diff, n2=n
            if diff in HashMap:                 #to check if the diff is present in nums(list)
                return [HashMap[diff], i]          #to return indices of n and the diff
            HashMap[n] = i                #update the hashmap in case the solution isn't found
        return                                    #the code works just fine without this line.
                                                     #add this line of code in case nums don't 
                                                     #contain required pair of integers