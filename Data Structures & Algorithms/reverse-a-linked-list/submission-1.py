# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
 
        if not head: #if head is pointing to null
            return None
        
        newHead = head 
        if head.next: #if head.next is not pointing to null (if we can keep reversing)
            newHead = self.reverseList(head.next) #reversing head.next
            head.next.next = head # reversing link between next node and head
        head.next = None
        return newHead