# Question：
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5




# Answer1:（简直智障，明明一行就能解决了，见Answer2。虽然Answer1代码行数巨多，但运行速度居然更快）
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        
        str=''
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if i ==0 and s[i] == " ":
                    # 针对s全部是“ ”
                    return 0
                continue 
                
            elif not s[i]==' ':
                for n in range(i,-1,-1):
                    if not s[n] ==' ':
                        str = str + s[n]
                        if n == 0:
                            # 针对从i开始到0都没有出现“ ”
                            return len(str)
                    elif s[n] ==' ':
                        return len(str)
# Answer2：
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])
        # see the function of strip() and split() 
