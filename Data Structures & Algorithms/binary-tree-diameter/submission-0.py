# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 #setting int value to be returned

        def dfs(root):#setting recursive funtion
            nonlocal res #bringing res variable into the dfs function

            if not root: #if there are no elements in the tree, there is no diamater
                return 0

            left = dfs(root.left) #left is the dfs function of the left side of the root
            right = dfs(root.right) #right is the dfs function of the right side of the root
            res = max(res, left + right) #we take the maximum result from the left and right side

            return 1 + max(left, right) #return the height of left and right

        dfs(root)
        return res