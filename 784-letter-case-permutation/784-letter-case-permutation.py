class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]          # create an empty list of string
        for i in s:                  # iterate through every character in s
            temp = []                # create an empty list inside the for loop
            if i.isalpha():        # check whether the given character is alphablet or number
                for j in res:          # for every string in a res
                    temp.append(j+ i.lower())         # add two types of character
                    temp.append(j+ i.upper())          #(upper and lower)
            else:                                   # if it is number
                for j in res:                       # for every str in res
                    temp.append(j+i)               # add the number to the str
            res = temp                            # add the temp list to res
        return res                                 # return the res
        
    # time complexity = O((2^N)*N)
    # space complexity = O ((2^N)*N)