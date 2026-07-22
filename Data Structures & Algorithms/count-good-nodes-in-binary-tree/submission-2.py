from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0
        queue = deque()
        queue.append((root, float("-inf")))
        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                res += 1
            if node.left:
                queue.append((node.left, max(max_val, node.val)))
            if node.right:
                queue.append((node.right, max(max_val, node.val)))
        return res

