# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return None
        stack = []
        self.result=0
        self.cnt = 0
        def dfs (root,k):
            if root==None:
                return   
            dfs(root.left,k)
            stack.append(root)
            self.cnt+=1
            if self.cnt==k:
                self.result = root.val
                return
            dfs(root.right, k)
        dfs(root,k)
        return self.result

