# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        path1 = []
        path2 = []
        def bactrack (root, target , path):
            # basecase
            
            if not root:
                return False
            # logic

            path.append(root)
            if root==target:

                return True

            if bactrack(root.left, target, path) or bactrack(root.right, target, path):
                return True
            # backtrack
            path.pop()
        # return False
        bactrack(root, p, path1)
        bactrack(root, q, path2)
        i=0
        while i<len(path1) and i <len(path2):
            if path1[i]==path2[i]:
                i+=1
            else:
                return path1[i-1]
        return path1[i-1]

        