class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        digits = [int(d) for d in str(x)]
        palindrome = digits[::-1]
        if digits == palindrome:
            return True