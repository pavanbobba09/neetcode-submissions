# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        if head.next is None:
            return head

        current = head
        dummy = None
        prev = dummy


        while current:
            nextPointer = current.next
            current.next = prev #change th direction
            prev = current
            current = nextPointer


        return prev

        