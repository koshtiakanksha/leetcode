class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)          # to store the length of the list
        stack = []                                  # create empty list 
        visited = [0] * n                           # add n times zero to visted
        count = 0                                   # set count to zero
        for i in range(n):                          # loop n times
            if visited[i] == 0:                     # since we don't want to repeat
                stack.append(i)                   # append index i to stack 
                while stack:                      # continue the loop till stack is not None
                    node = stack.pop() # a new vari that stores the recentmost val in stack
                    visited[node] = 1     # set the visited at index node equal to one
                    for j in range(n):       # for column
                        if isConnected[node][j] == 1 and visited[j] == 0:
                            stack.append(j)          # we add jth index to stack
                count += 1                      # if while loop executes we add 1 to count
        return count                         # we return count
        
        # time complexity = O(N**2)
        # space complexity = O(N)