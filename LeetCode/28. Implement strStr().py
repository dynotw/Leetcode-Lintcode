# Question:
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack, or return 0 when needle is empty.
"""The first of occurrence means the first index when needle occurs in haystack """




# Answer:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if needle in haystack:
            # if needle[0] in haystack:
            # return haystack.index(needle[0])
                # for i in len(aystack):
                #     for j in len(needle):
                #         if haystack[i] == needle[j]:
                """The above are wrong code, which is programmmed when I misunderstand the question"""
            return haystack.find(needle)
            # defination 'find' return the first index where 'needle' occur
                            
        else:
            return -1
