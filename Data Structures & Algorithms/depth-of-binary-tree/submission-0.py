# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        max_depth = 0

        while q:
            node, depth = q.popleft()

            if not node:
                continue

            max_depth = max(max_depth, depth)

            if node.left:
                q.appendleft((node.left, depth + 1))
            if node.right:
                q.appendleft((node.right, depth + 1))
        
        return max_depth