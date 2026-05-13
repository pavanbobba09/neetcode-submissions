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
        prevNode = None
        nextNode = None

        while current:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode

        return prevNode

        
    


        
        