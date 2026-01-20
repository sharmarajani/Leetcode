# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev=None
        self.first=None
        self.second = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack =[]
        while stack or root:
            while root:
                stack.append(root)
                root= root.left
            root = stack.pop()
            if self.prev and self.prev.val > root.val:
                if not self.first :
                    self.first = self.prev
                self.second = root

            self.prev = root
            root = root.right
        self.first.val, self.second.val = self.second.val, self.first.val


        