# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,f = head, head
        while f and f.next:
            s = s.next           # slow moving pointer
            f = f.next.next     # fast moving pointer
            if s == f:     # if they are linked cycle both pointers will point at same
                return True
        return False
    
    # time complexity = O(N); N= no of nodes 
    # space complexity = O(1)