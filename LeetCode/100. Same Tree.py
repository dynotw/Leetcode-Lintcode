# Question:
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.






# Answer：
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(p, q):
            if p == None and q != None:
                return False
            if p != None and q == None:
                return False
            if p == None and q == None:
                return True
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        # Recursion，即函数自己调用自=自己。此二叉树并非例子如此简单，可能还有更多层。
        
        return dfs(p,q)
