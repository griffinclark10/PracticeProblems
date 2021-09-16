#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#s consists of only lowercase letters

#worked for every case except if the duplicate isn't found before the last element of the string
# def firstUniqChar(s):         
#         """
#         :type s: str
#         :rtype: int
#         """
#         add = 1
#         for letter in s:
#             if s.find(letter, add) != -1:
#                 add += 1
#             else: 
#                 return (add -1)
#         return -1


#found in leetcode answers
def firstUniqChar(s):
    letters='abcdefghijklmnopqrstuvwxyz'
    index =[s.index(l) for l in letters if s.count(l) == 1] #making a list of the indecies of the letters in s that aren't repeated
    return min(index) if len(index) > 0 else -1 #return the lowest index

#testing
s = "leetcode" 
print(firstUniqChar(s))

