# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recurse
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf

        def helper(root):
            # base
            if not root:
                return True
            # recurse
            if not helper(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return helper(root.right)
        return helper(root)