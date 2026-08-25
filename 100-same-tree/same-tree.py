# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu1 = deque()
        qu2 = deque()
        if not p and not q:
            return True
        if p:
            qu1.append(p)
        if q:
            qu2.append(q)
        while qu1 or qu2:
            if len(qu1)!=len(qu2):
                return False
            for _ in range(len(qu2)):
                node1 = qu1.popleft()
                node2 = qu2.popleft()
                if node1.val != node2.val:
                    return False
                l1 = node1.left 
                r1 = node1.right
                l2 = node2.left
                r2 = node2.right

                if (l1 is None and l2 is not None) or (l2 is None and l1 is not None) or (r1 is None and r2 is not None) or (r2 is None and r1 is not None):
                    return False
           
                if l1:
                    qu1.append(l1)
                if r1:
                    qu1.append(r1)
                if l2:
                    qu2.append(l2)
                if r2: 
                    qu2.append(r2)
        return True
             
        