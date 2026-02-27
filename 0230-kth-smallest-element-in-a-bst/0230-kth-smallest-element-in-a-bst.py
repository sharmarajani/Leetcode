# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return -1
        q=[]
        # q.append(root)
        while root or len(q)>0:
            while root:
                q.append(root)
                root=root.left
            root=q.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
        return -1

        