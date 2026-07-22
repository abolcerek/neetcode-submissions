# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: #if head = null
            return None

        newHead = head #setting up variable to be used later as the response
        if head.next: #if head.next doesnt = null
            newHead = self.reverseList(head.next) #recursive call that reversed list
            head.next.next = head #reversing the link between next node and head
        head.next = None
        return newHead
