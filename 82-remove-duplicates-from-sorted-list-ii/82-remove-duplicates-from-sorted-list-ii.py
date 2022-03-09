# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)     # we add 0 at the beginning of the listnode
        curr = dummy                  # shows us the last node
        
        while head:                   
            if head.next and head.next.val == head.val:  # if we find duplicates
                while head.next and head.next.val == head.val:    # we skip all duplicates
                    head = head.next                    # move till the end of duplicates
                curr.next = head.next     
            else:
                curr = curr.next     # if its not duplicate, we move our curr
            head = head.next         # to check the next val
        return dummy.next            # since the first node is zero
    
    # time complexity = O(N)
    # space complexity = O(1)