Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842, and since the decimal part is truncated, 2 is returned.




Answer:
class Solution:
    def mySqrt(self, x: int) -> int:
        y = int(x**(1/2))
        return y
        # 跟取整有关的函数：1、向下取整：int()； 2、向上取整：ceil()；3、四舍五入：round()；4、将整数部分和小数部分分别取出，可以使用math模块中的 modf()方法
