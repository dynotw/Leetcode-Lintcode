# Question:(it's the derivative of 102 Problems)
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]





# Answer:
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        ans = []
        def bfs(root,level):
            if root != None:
                
                if len(ans) < level + 1:
                    ans.append([])
                    
                # 为了append[level]不出现 out of index，需要根据level情况给ans添加元素，使得存在ans[level]
                # 针对这里的递归，都是先运行bfs.left，即对于相应的level，在运行bfs.left已经创建了ans[level]
                # 可是后续我们还要运行bfs.right，而对应level的bfs.right与bfs.left是共享一个ans[level]的
                # 所以不需要再重复创建ans[level]，因此这个if语句块是判断是否需要创建ans[level]的
                
              
                
                ans[level].append(root.val)
                #不是将对象直接加入ans列表而是添加到ans列表中对应的列表对象中
                
                bfs(root.left,level + 1)
                bfs(root.right,level + 1)
                
        bfs(root,0)
        ans.reverse()
        return ans
