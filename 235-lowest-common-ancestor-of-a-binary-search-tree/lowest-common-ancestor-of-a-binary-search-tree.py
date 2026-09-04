# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qu = deque()
        qu.append([root])
        neededpath = [] 
        while qu:
            node_path = qu.popleft()

            if node_path[-1] == p or node_path[-1] == q:
                neededpath.append(node_path)
            
            if node_path[-1].left:
                qu.append(node_path + [node_path[-1].left])

            if node_path[-1].right:
                qu.append(node_path + [node_path[-1].right])
        path1 = neededpath[0]
        path2 = neededpath[1]
        ans = 0
        for i in range(min(len(path1),len(path2))):
            if path1[i] == path2[i]:
                ans = path1[i]
            else:
                break
        return ans
                    
            
        