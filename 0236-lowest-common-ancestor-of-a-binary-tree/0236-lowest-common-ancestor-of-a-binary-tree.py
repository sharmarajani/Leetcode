# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        def backtrack (root, p,q, arraylist):
            # base case
            if path1 and path2:
                return True
            if root==None:
                return False
            # action
            arraylist.append(root)
            if root==p:
                path1.extend(arraylist[:])
            if root==q:
                path2.extend(arraylist[:])
            
            # logic
            
            if backtrack(root.left, p, q, arraylist) or backtrack(root.right, p, q, arraylist):
                return True
            # backtrack
            arraylist.pop()
            return False
            
        backtrack(root, p,q, [])
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                return path1[i - 1]
            i += 1
        return path1[i - 1] if i > 0 else None

        