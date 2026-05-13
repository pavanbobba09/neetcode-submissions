# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #form above code we know out middle element is slow pointer

        prevNode,curr = None,slow

        while curr:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode

        #here at prevNode we are having the reverse of second half

        first,second = head, prevNode

        while second.next:
            firstTemp = first.next
            secondtemp = second.next

            first.next = second
            second.next = firstTemp

            first = firstTemp
            second = secondtemp

        
