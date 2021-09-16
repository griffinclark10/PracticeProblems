#Write a function that reverses a string. The input string is given as an array of characters s.


# def reverseString(s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         str = ""
#         newList = []
#         for ele in s: str += ele
#         newstr = str[::-1]
#         for ele in newstr: newList.append(ele)
#         s = newList
#         print(s)

def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)
        


#testing
s = ["d","a","v","i","d"]

reverseString(s)