# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        root_subtree = None

        while stack:
            root_subtree = stack.pop()

            if not root_subtree:
                continue
            
            # if root_subtree.val != subRoot.val:
            stack.append(root_subtree.left)
            stack.append(root_subtree.right)
                # continue

            print('match', root_subtree.val)
            
            sub_stack = [(root_subtree, subRoot)]
            is_subtree = True
            while sub_stack:
                og, sub = sub_stack.pop()

                if not og and not sub:
                    continue
                
                if not og or not sub or og.val != sub.val:
                    is_subtree = False
                    break
                
                sub_stack.append((og.left, sub.left))
                sub_stack.append((og.right, sub.right))
            
            if is_subtree:
                return True
        return False
