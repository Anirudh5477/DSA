# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 1
        q = deque()
        q.append((root,root.val))
        while q:
            node, max_path = q.popleft()
            if node.left:
                if node.left.val >= max_path:
                    ans += 1
                    q.append((node.left,node.left.val))
                else:
                    q.append((node.left, max_path))

            if node.right:
                if node.right.val >= max_path:
                    ans += 1
                    q.append((node.right,node.right.val))
                else:
                    q.append((node.right, max_path))            
        return ans
        