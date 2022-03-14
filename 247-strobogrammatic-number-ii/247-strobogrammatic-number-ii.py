class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversible_pairs = [
            ['0', '0'], ['1', '1'], 
            ['6', '9'], ['8', '8'], ['9', '6']
        ]
        
        length = n % 2
        
        q = ["0", "1", "8"] if length == 1 else [""]
        
        while length < n:
            length += 2
            next_level = []
            
            for number in q:
                for pair in reversible_pairs:
                    if length != n or pair[0] != "0":
                        next_level.append(pair[0] + number + pair[1])
            q = next_level
            
        return q
                        
        # time complexity = O(N)
        # space complexity = O(N)