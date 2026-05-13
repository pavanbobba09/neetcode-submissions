# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverLL(self, head):
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Step 1: reverse the linked list
        newHead = self.reverLL(head)

        # Step 2: delete nth node from start
        if n == 1:
            newHead = newHead.next
        else:
            temp = newHead
            count = 1
            while count < n - 1 and temp and temp.next:
                temp = temp.next
                count += 1

            if temp.next:
                temp.next = temp.next.next

        # Step 3: reverse again to restore original list
        return self.reverLL(newHead)
