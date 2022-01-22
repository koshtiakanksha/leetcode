class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        stack = []
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                stack.append(i)
                while stack:
                    node = stack.pop()
                    visited[node] = 1
                    for j in range(n):
                        if isConnected[node][j] == 1 and visited[j] == 0:
                            stack.append(j)
                count += 1
        return count
        