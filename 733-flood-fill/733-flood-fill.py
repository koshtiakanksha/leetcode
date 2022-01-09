class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]                  # save the integer of the given row and column
        if color == newColor: 
            return image             # since both are equal, we can return the original image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor         # if the element in that position has the same                                             color as the given element, update it to newcolor
                if r >= 1: 
                    dfs(r-1, c)                               # up
                if r+1 < len(image):                          # len(image)=> no. of rows
                    dfs(r+1, c)                               # down
                if c >= 1: 
                    dfs(r, c-1)                              # left
                if c+1 < len(image[0]):                      # len(image[0])=> no. of columns
                    dfs(r, c+1)                             #right

        dfs(sr, sc)
        return image                           # returns the updated image
        