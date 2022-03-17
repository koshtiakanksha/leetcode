class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = bal = 0
        for i, x in enumerate(s):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if s[i-1] == '(':
                    ans += 1 << bal
        return ans
    
    # time complexity = O(N)
    # space complexity = (1)
        