class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        temp = dummyNode
        carry = 0

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            temp.next = ListNode(sum % 10)
            temp = temp.next

        return dummyNode.next
