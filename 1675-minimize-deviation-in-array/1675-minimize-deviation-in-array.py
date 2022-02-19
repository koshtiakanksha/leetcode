class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        possible_list = []
        for num in nums:
            candidates = []
            if num % 2 == 0:
                temp = num
                candidates.append(temp)
                while temp % 2 == 0:
                    temp //= 2
                    candidates.append(temp)
            else:
                candidates.append(2*num)
                candidates.append(num)
            possible_list.append(candidates[::-1])
            
        pointers = [(candidate, index, index_in_candidates) for index, 
                    candidates in enumerate(possible_list) 
                    for index_in_candidates, candidate in enumerate(candidates)]
        pointers.sort()
        min_deviation = inf
        current_end = max(candidates[0] for candidates in possible_list)
        
        for current_start, index, index_in_candidates in pointers:
            if current_end - current_start < min_deviation:
                min_deviation = current_end - current_start
                
            if index_in_candidates +1 == len(possible_list[index]):
                return min_deviation
            next_value = possible_list[index][index_in_candidates + 1]
            current_end = max(current_end, next_value)
        