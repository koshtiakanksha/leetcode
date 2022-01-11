# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)         # adding a node before head, (can put any value)
        prev = dummy                       # naming the pointers
        curr = head
        
        while curr and curr.next:
            nxtpair = curr.next.next         # as these keep on updating, we need to save it 
            second = curr.next
            
            second.next = curr
            curr.next = nxtpair
            prev.next = second
            
            prev = curr                    # updating these for another loop
            curr = nxtpair
        return dummy.next  # since we do not want to return a node we added in the first step
         
        
        # time complexity: O(n)