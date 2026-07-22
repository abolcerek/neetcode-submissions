# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set
        # temp = head
        # while temp.next != null
            # if temp.next not in set
                #add to the set
            # if temp.next.val in the set
                # return true
        #return false

        # head = [1,2,2,3,4], index = 1

        hashset = set()
        if head == None:
            return False

        temp = head
        while temp.next != None:
            if temp.next not in hashset:
                hashset.add(temp.next)
            else:
                return True
            temp = temp.next
        return False