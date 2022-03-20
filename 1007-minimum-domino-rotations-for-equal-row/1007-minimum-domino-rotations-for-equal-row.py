class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            
            rotations_a = rotations_b = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_a += 1
                elif bottoms[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
    
        n = len(tops)
        rotations = check(tops[0]) 
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations 
        else:
            return check(bottoms[0])
        
        
        # time complexity = O(N)
        # space complexity = O(1)
        