class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        
        for i in range(query_row + 1):
            for c in range(i + 1):
                q = (A[i][c] - 1.0) / 2.0
                
                if q > 0:
                    A[i+1][c] += q
                    A[i+1][c+1] += q
                    
        return min(1, A[query_row][query_glass])
    
    # time complexity = O(r**2) or O(1) ; r is the number of rows and since we know r
    # space complexity = O(r**2) or O(1) ; r is the number of rows and since we know r