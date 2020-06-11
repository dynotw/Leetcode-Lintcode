# Question:
# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.




# Answer:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
            # return the first index where target occurs 
        
        a = False
        # 'a' is for the situation that target is bigger than all element in nums, so target must insert in the back of nums
        
        for i in range(len(nums)):
            # Don't forget use range(0), otherwise there will be no loop
            if target <= nums[i]:
                a = True
                return i
        
        if not a:
            return len(nums)
