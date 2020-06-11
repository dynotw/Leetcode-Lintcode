Question:
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.





Answer:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i +=1
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         del nums[i]
        """Important Notice: can use 'while' rather than'for', 
        because 'for' will only use the value of len(nums) which is calucated in the first time
        when the code(del nums[i]) runs, the true length of nums has substract 1, but 'for' still use the first length rather than new
        so that nums[i] and nums[i-1] will warn list index out of range
        However, 'while' will run len(nums) in the beginning of each loop, so valuse of len(nums) will update, when the code(del nums[i]) runs"""
        
        for n in range(len(nums)):
            print(nums[n])
