#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#taken from discussion
def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower() #e.isalnum() makes sure that the string has only letters & numbers, .lower makes it lowercase
        return s==s[::-1]
        


#testing
s = "I // HaveSo MucHHHH to !! do. )(*&^%$#"
print(isPalindrome(s))