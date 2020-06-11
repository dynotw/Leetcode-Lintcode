Question:
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"




Answer:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    # int(x, base=10):  x -- 字符串或数字; base -- 进制数，默认十进制。
    # bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
    # [2:]是索引的表达，从索引2开始到最后
    
