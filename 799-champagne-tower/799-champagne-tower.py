class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]     # [[0], [0, 0], [0, 0, 0], .....]
        A[0][0] = poured           # the value at zeroth index of the first list in A
        
        for i in range(query_row + 1):           # iterate through the range
            for c in range(i + 1):               # iterate through the range
                q = (A[i][c] - 1.0) / 2.0        # since it will fall off in two glasses
                
                if q > 0:
                    A[i+1][c] += q              # update the values
                    A[i+1][c+1] += q
                    
        return min(1, A[query_row][query_glass])
    
    # time complexity = O(r**2) or O(1) ; r is the number of rows and since we know r
    # space complexity = O(r**2) or O(1) ; r is the number of rows and since we know r