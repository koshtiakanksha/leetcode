# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:                   # if it is an empty listnode
            return None
        newhead = head                
        if head.next:                 # if the next element to the current ne exists
            newhead = self.reverseList(head.next)        # call a function for head.next
            head.next.next = head          
        head.next = None               # point it to null to avoid endless loop
        return newhead
    
    # time complexity = O(n)
    # space complexity = O(n)
            