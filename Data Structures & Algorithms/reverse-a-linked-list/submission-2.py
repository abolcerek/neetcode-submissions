# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head #prev points to null, curr points to head

        while curr: #while curr is not null
            temp = curr.next #declaring temp value which is set to curr.next
            curr.next = prev #reversing the pointer 
            prev = curr #moving prev up the list
            curr = temp #moving curr up the list
        return prev