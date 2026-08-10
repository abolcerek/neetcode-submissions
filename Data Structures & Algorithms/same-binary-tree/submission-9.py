from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def BFS(root1, root2):
            queue = deque([[root1, root2]])
            while queue:
                levels = len(queue)
                for _ in range(levels):
                    curr1, curr2 = queue.popleft()
                    if curr1.val != curr2.val:
                        return False
                    if curr1.left and curr2.left:
                        if curr1.left.val == curr2.left.val:
                            queue.append([curr1.left, curr2.left])
                        else:
                            return False
                    if curr1.right and curr2.right:
                        if curr1.right.val == curr2.right.val:
                            queue.append([curr1.right, curr2.right])
                        else:
                            return False
                    if curr1.left and not curr2.left:
                        return False
                    if curr1.right and not curr2.right:
                        return False   
                    if curr2.left and not curr1.left:
                        return False
                    if curr2.right and not curr1.right:
                        return False 
                     
            return True
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        return BFS(p, q)