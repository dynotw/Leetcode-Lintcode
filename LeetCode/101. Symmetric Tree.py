# Question:
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
 
# Note: Bonus points if you could solve it both recursively and iteratively.





# Answer1(Recursive):
# compared to Problem 100
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # compared to problem 100.same tree
        def solve(p,q):
            if p == None and q != None:
                return False
            if p != None and q == None:
                return False
            if p == None and q == None:
                return True
            if p.val != q.val:
                return False
            
            return solve(p.left,q.right) and solve(p.right,q.left)
            
        
        if root == None:
            return True
        else:
            return solve(root.left,root.right)

# Answer2(Iteration):
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # compared to problem 100.same tree
        if not root : return True
        stack = [root.left,root.right]
        while stack:
            node1,node2 = stack.pop(), stack.pop()
            if not node1 and not node2: continue
            if not node1 or not  node2 : return False
            if node2.val != node1.val : return False
            stack += [node1.left, node2.right, node1.right,node2.left]
            # 联系 ‘if if not node1 and not node2: continue’ 就可以理解：为什么这里的stack赋值与while循环外的stack初始化赋值不同
            # 因为root是最初的点，一个点只能有left，right两个element
        return True
    
