# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()              # to create an empty listnode
        tail = dummy                    # to get access to the first element
        while l1 and l2:                # only when both l1 and l2 exists
            if l1.val < l2.val:          
                tail.next = l1         
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
    
    # time complexity = O(m *n) length of two lists
    # space complexity = O(n)
        