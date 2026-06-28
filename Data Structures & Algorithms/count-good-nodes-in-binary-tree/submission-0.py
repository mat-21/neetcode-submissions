# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-infinity'))]

        good_nodes = 0

        while stack:
            node, max_value = stack.pop()

            if not node:
                continue
            
            if node.val >= max_value:
                good_nodes += 1

            stack.append((node.right, max(max_value, node.val)))
            stack.append((node.left, max(max_value, node.val)))

        return good_nodes
