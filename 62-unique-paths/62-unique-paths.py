class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row [0]
   

    # time complexity = O(m*n)
    # space complexity = O(m*n)
    
    # explaination:
    # let m = 3 and n = 7
    # row = bottom row = [1, 1, 1, 1, 1, 1, 1]
    # i = 0 -> newRow = [1, 1, 1, 1, 1, 1, 1]
        # j = 5 -> newRow = [1, 1, 1, 1, 1, 2, 1]
        # j = 4 -> newRow = [1, 1, 1, 1, 3, 2, 1]
        # j = 3 -> newRow = [1, 1, 1, 4, 3, 2, 1]
        # j = 2 -> newRow = [1, 1, 5, 4, 3, 2, 1]
        # j = 1 -> newRow = [1, 6, 5, 4, 3, 2, 1]
        # j = 0 -> newRow = [7, 6, 5, 4, 3, 2, 1]
    # i = 1 -> newRow = [1, 1, 1, 1, 1, 1, 1]
        # j = 5 -> newRow = [1, 1, 1, 1, 1, 3, 1]
        # j = 5 -> newRow = [1, 1, 1, 1, 6, 3, 1]
        # j = 5 -> newRow = [1, 1, 1, 10, 6, 3, 1]
        # j = 5 -> newRow = [1, 1, 15, 10, 6, 3, 1]
        # j = 5 -> newRow = [1, 21, 15, 10, 6, 3, 1]
        # j = 5 -> newRow = [28, 21, 15, 10, 6, 3, 1]
    # row = newRow -> row = [28, 21, 15, 10, 6, 3, 1]
    # row[0]= 28

    
        