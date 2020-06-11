# Question:
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]





# Answer:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
         ans=[]
         def lo(root,level):
                if root != None:
                    if len(ans) < level+1:
                        ans.append([])
                        
                    ans[level].append(root.val)
                    lo(root.left, level+1)
                    lo(root.right, level+1)
         
         level = 0
         lo(root, level)
         return ans
         # have to return the list named ans, because the function(lo) dosen't return specific element.         
