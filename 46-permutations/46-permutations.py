class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []                           # create an empty list
        if len(nums) == 1:             # if the length is 1 we return the copy of nums         
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)                   # we pop the first element in the list
            perms = self.permute(nums)   # call the function for perms and set it inside a var
            for perm in perms:             # go through each value in the above set var
                perm.append(n)             # append the first element of the list to perm
            result.extend(perms)           # add it to the res
            nums.append(n)  # since we remove it in the beginning, we are adding it at the end
        return result
        