# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       diameter = [0]
       def diameter_finder(root):
           if root.left:
              l = diameter_finder(root.left) 
           else:
              l = 0
           if root.right:
              r = diameter_finder(root.right) 
           else:
              r = 0
           if l + r > diameter[0]:
               diameter[0] = l + r
           return max(l+1,r+1)
       diameter_finder(root)
       return diameter[0]

        
        