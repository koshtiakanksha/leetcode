class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": 
            return []      # if empty str we return empty array
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '1': '','0': ''}   # we create a dict mapping the letters to given numbers
        replies = [c for c in phone[digits[0]]] # print(replies)= [a, b, c] for digits='23'
        for i in range(1, len(digits)):
            temp = []                   # empty array before every loop
            for p in phone[digits[i]]: # start with index 1 and not index 0, since 0 is added 
                for r in replies:         # we add these leeters to every letter in replies 
                    temp.append(r + p)  # print(temp) =[ab]->[ad,ae]->[ad,ae,af]----
            replies = temp.copy()       # add copy of temp to replies 
        return replies                  # and return our replies
    
# time complexity = O((4^N)N)   because of digits 7 and 9 having 4 letters each.
# space complexity = O(N)   N is the length of digits
        