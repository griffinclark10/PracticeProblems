#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "": return 0
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
        
    


#true
h = "hello"
n = "h"
strStr(h,n)