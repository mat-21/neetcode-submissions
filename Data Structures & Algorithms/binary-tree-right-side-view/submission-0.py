# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            len_q = len(q)
            
            last_node = None
            for i in range(len_q):
                node = q.popleft()

                if not node:
                    continue

                q.append(node.left)
                q.append(node.right)

                last_node = node

            if last_node:
                res.append(last_node.val)
        
        return res                

