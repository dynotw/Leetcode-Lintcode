# Question:
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.




# Answer1:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        sum = 0
        
        for i in range(len(digits)):
            sum = sum + digits[i]*(10**(len(digits)-i-1))
        
        sum = sum + 1
        
        string = str(sum)
        
        list = []
        
        for n in string:
            list.append(n)
        
        return list

#Answer2:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length = len(digits)
        if length == 0:
            return [1]
        # 空列表
        carry = 0
        digits[length - 1] += 1
        # 个位数+1
        
        while length > 0:
            digits[length - 1] += carry
            # length update every loop
            # the value of carry may change during the loop(if 语句)
            if digits[length - 1] > 9:
                # 判断是否进位
                carry = 1
                digits[length - 1] = 0
            else:
                carry = 0
                break
            
            length -= 1
            # 结合while loop， 从右到左遍。
            
        if carry == 1:
            digits.insert(0, 1)
            # 添加一位，9999的情况。while loop不是通过break退出，是length <0 导致loop结束
            
        return digits
