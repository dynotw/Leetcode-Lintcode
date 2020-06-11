# Question:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Important Notice: The problem is a liitle interesting.



# Answer1（直接暴力法）:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length   
        # dp[i]表示以nums[i]结尾的子序列的最大和
        dp[0] = nums[0]
        # 先将第一个element认为是最大的subarray
        maxsum = dp[0]
        # dp是当前最大值，maxsum是最终最大值
        
        for i in range(1, length):
            # 已经假设第一元素是最大的subarray， 所以从第二元素开始循环
            if dp[i - 1] + nums[i] >= nums[i]:
                dp[i] = dp[i - 1] + nums[i]
                # dp[i]不是我们的最终输出值，maxsum才是
                # 当if成立时，我们可以把dp[i-1]+nums[i]看做是一个element，x
                # 对于nums[i+1]而言，+x > + nums[i]
                
            else:
                dp[i] = nums[i]
                # 相当于subarray断了，从nums[i]重新开始计算sum
                
            if dp[i] >= maxsum:
                # 因为有可能d[i-1]+nums[i]>nums[i], but < dp[i-1]
                # so updated dp[i] may less than the exsited maxsum
                maxsum = dp[i]
             
        return maxsum     


# Answer2（分治算法思想）:
# 将数组划分左右两部分，最大子序列和有三种情况，1)在左侧部分；2)在右侧部分；3)跨左右两部分
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divideMethod(nums, 0, len(nums) - 1)
 
    def divideMethod(self, nums, i, j):
        if i == j:
            return nums[i]
        divide = (i + j) // 2
        
        ls = nums[divide]
        rs = nums[divide + 1]
        sum = 0
        for k in range(divide + 1, j + 1):
            # 从左到右计算，sums的右侧部分
            sum += nums[k]
            if sum >= rs:
                rs = sum
        sum = 0
        for k in range(divide, i - 1, -1):
            # 从右向左计算，sums的左侧部分
            sum += nums[k]
            if sum >= ls:
                ls = sum
        maxSum = ls + rs
        # 这个maxsum是跨左右两部分的最大
        leftMaxSum = self.divideMethod(nums, i, divide)
        # 对左侧也重复使用分支算法思想
        rigthMaxSum = self.divideMethod(nums, divide + 1, j)
        
        if leftMaxSum >= maxSum:
            maxSum = leftMaxSum
        if rigthMaxSum >= maxSum:
            maxSum = rigthMaxSum
        # 确定最大subarray是3种情况中的哪一种
        
        return maxSum

