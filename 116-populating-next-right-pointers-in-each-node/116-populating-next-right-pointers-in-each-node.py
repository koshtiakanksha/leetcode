"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections                                   #very important step

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:                             
            return None
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size-1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
        
        
        