# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative in-order
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True
        


