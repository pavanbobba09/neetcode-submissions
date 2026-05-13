# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reversing(self,head):
        temp = head
        prev = None

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        return prev

    def findMiddle(self, head):
        temp = head
        slow = head
        fast = head

        #first lets find the middle element

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow #middle elemt
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #if head is non
        if head is None:
            return None

        if head.next is None:
            return None

        temp = head

        #findingMiddleElemt 
        middleElement = self.findMiddle(head)
        

        #lets reverse the middle element
        startingPointer = self.reversing(middleElement)
        
        temp_nextNode = None
        t2 = startingPointer

        #lets start giving connection
        while temp and t2:
            temp1 = temp.next
            second = t2.next

            temp.next = t2

            if temp1 is None:
                break

            t2.next = temp1

            temp = temp1
            t2 = second

        if temp:
            temp.next = None
            



            


        
        



        

