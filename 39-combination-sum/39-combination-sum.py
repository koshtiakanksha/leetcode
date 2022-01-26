class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))  # make a deep copy of the current combination
                return                       # since it is a base case   
            elif remain < 0:            # we stop here and return nothing
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])   # add the number into the combination
                backtrack(remain - candidates[i], comb, i)   # try with the same val again
                comb.pop()       # remove the last added val

        backtrack(target, [], 0)    # to begin with we call the fun for given parameters

        return results
    
    # time complexity = O(N^((T/M)+1)
    # space complexity = O((T/M))
    # Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.