# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 
        sumi = 0
        def helper (root, curr_sum):
            nonlocal sumi
            if root is None:
                return
            curr_sum = curr_sum* 10 + root.val
            helper(root.left, curr_sum)
            if root.left is None and root.right == None:
                sumi+= curr_sum
            helper(root.right, curr_sum)
        helper (root, 0)
        return sumi

        