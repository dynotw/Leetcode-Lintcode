# Question:
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

"""n>1时，对于每一个台阶i，要到达台阶，最后一步都有两种方法，从i-1迈一步，或从i-2迈两步。

　　也就是说到达台阶i的方法数=达台阶i-1的方法数+达台阶i-2的方法数。"""




# Answer:
class Solution:
    def climbStairs(self, n: int) -> int:
        # 答案为Fibonacci数列: 1,1,2,3,5,8,13,21......
        
        list = [1,2]
        
        if n <=1:
            return 1
        
        if n ==2:
            return 2
        
        for i in range(n-2):
            
            list.append(list[-1]+list[-2])
        
        return list[-1]
