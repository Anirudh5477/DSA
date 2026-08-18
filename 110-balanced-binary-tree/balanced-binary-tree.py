# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isb(root):
            if root.left is None and root.right is None:
                return 1
            if root.left:
                l = isb(root.left)
                if not l:
                    return False
            else:
                l = 0
            if root.right:
                r = isb(root.right)
                if not r:
                    return False
            else:
                r = 0
            if not (-1 <= l - r <= 1):
                return False 
            
            
            return max(l,r) + 1
        ans = isb(root)
        if not ans:
            return False
        return True
