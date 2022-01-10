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
        if not root:                     # if the root doesn't exist we simply return None   
            return None
        q = collections.deque([root])     # initializing the queue data structure
        while q:
            size = len(q)                # note the size of q. very important
            for i in range(size):
                node = q.popleft()        #to pop the from the front of the queue
                if i < size-1:         # to avoid establishing new pointers beyond the end
                    node.next = q[0]    
                if node.left:            #to add the children at the end
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
        
        
        