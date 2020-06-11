Question:
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.





Answer1(Recursion):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def fd(x,depth):
            if x == None:
                return depth
            if x != None:
                depth += 1
            
            return max(fd(x.left,depth),fd(x.right,depth))
        
        depth = 0
        return fd(root, depth)
        
        
"""The following code doesn't work, because it only has two direction: left-left-left-.... or right-right-right-right-...
no left and right alternating"""        
#         def fd_r(x, depth_r):
#             if x ==None:
#                 return depth_r
            
#             if x != None:
#                 depth_r += 1 
            
#             if x.right != None:
#                 depth_r += 1
            
#             return fd_r(x.right,depth_r)
        
#         def fd_l(x, depth_l):
#             if x ==None:
#                 return depth_l
            
#             if x != None:
#                 depth_l += 1
            
#             if x.left != None:
#                 depth_l += 1
            
#             return fd_l(x.left,depth_l)
        
#         depth = 0
        
#         a=fd_l(root,depth)
#         b=fd_r(root,depth)
        
#         return max(a,b)
