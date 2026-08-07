from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def BFS(root):
            queue = deque([root])
            depth = 0
            while queue:
                layers = len(queue)
                for _ in range(layers):
                    curr = queue.popleft()
                    print(curr.val)
                    children = get_children(curr)
                    for child in children:
                        print(f'This is child: {child.val}')
                        queue.append(child)
                depth += 1
            return depth
        def get_children(root):
            children = []
            if root.left is not None:
                children.append(root.left)
            if root.right is not None:
                children.append(root.right)
            return children
        if not root:
            return 0
        return BFS(root)
