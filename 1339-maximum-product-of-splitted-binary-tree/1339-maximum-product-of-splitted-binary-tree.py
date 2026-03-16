# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def get_sum (node):
            if not node:
                return 0
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            curr_sum = node.val + left_sum + right_sum
            sums.append(curr_sum)
            return curr_sum
        total_sum = get_sum(root)
        max_prod = 0
        for s in sums:
            max_prod = max(max_prod , s * ( total_sum - s))
        return max_prod % (10**9 + 7)
        