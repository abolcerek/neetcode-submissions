# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        curr = head
        while curr:
            if curr.next in hashset:
                return True
            else:
                hashset.add(curr.next)
                curr = curr.next
        return False