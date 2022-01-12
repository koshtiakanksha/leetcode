# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head                                      # initializing the pointers
        while curr:                                  # while there are elements to reverse
            nxt = curr.next                      
            curr.next = prev
            prev = curr                            # reversing the elements
            curr = nxt
        return prev
    
    # time complexity = O(n)
    # space complexity = O(1)
    
    # time complexity = O(n)
    # space complexity = O(n)
            