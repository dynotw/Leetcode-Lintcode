# Question:
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string. The question is hard to understand, please see some explanation on website





# Answer:
class Solution:
    def countAndSay(self, n: int) -> str:
        b='1'   
        # 将第一行的1换成字符串类型，便于下一行的读出
        for i in range (n-1):   
            # (n-1)是因为第一行不需要处理，直接可以读出
            """这个loop非常巧妙，相当于‘n+1’都会重复‘n’的所有步骤；即‘n+1’是在‘n’的基础上多跑一轮loop"""
            # 每次loop的b都是update的，because there is the code(b=c) at the bottom of the loop
            a,c,count=b[0],'',0 
            # 同时对a，c，count赋值
            """a用来读取上一行的第一个字符，先对b(str)中的第一个数字进行统计；a的值在loop中可能会改变
            c用来存放读出的内容(str)，
            count用来统计"""
            for j in b:   
                if a==j:
                    count += 1
                    # 这计数直到j不等于a，即b（str）中开始出现新的数字
                else:
                    c += str(count)+a   
                    # 先把b（str）中已经计数过的数字，以题目要求的表达形式以string的方式储存在c
                    #注意一定要将count转换为字符串型，否则两个数就会相加（变成数学公式）。
                    a=j
                    # 重新给a赋值，相当于要对一个新的数字进行计数，因为b(string)中出现了新的数字（即j不等于a）
                    count=1
                    # else语句的执行，说明是新数字的第一次出现。若新数字还会继续出现，则在新的loop中将run if语句，因为a已经被赋值为j
            c += str(count)+a
            b=c
        return b

