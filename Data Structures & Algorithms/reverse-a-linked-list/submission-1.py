# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        # Step 1: Store all values in a list
        lst = []
        temp = head
        while temp is not None:
            lst.append(temp.val)
            temp = temp.next

        # Step 2: Reverse the list
        lst.reverse()

        # Step 3: Build new linked list from reversed values
        new_node = ListNode(lst[0])
        curr = new_node

        for x in lst[1:]:
            curr.next = ListNode(x)
            curr = curr.next

        return new_node
