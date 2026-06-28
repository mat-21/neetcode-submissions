# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = deque([root])

        while q:
            node = q.popleft()
            
            if not node:
                continue

            print(node.val)

            tmp_left = node.left if node else None
            tmp_right = node.right if node else None
            node.left = tmp_right
            node.right = tmp_left
            
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        return root