# Question:
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
             
             


# Answer(Sliding windows):
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        slen = len(s)
        if slen == 0:
            return 0
        i = j = 0
        charlist = set()
        maxlen = 0
        while i < slen and j < slen:
        # str[i:j+1]组成了charlist
            # 如果尾字符出未现在集合中，加入集合，指针后移
            if s[j] not in charlist:
                charlist.add(s[j])
                maxlen = max(maxlen, j - i + 1)
                j += 1
            else:
                # 如果尾字符出现在集合当前，由于不知道出现在前面哪个位置，所以从前面依次移除字符。
                charlist.remove(s[i])
                i += 1
        return maxlen
