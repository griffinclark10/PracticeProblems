#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sSort = sorted(s)
        tSort = sorted(t)
        if tSort == sSort:
            return True 
        return False

def isAnagram2(self, s, t): #this one works with all characters in unicode, not just lowercase english letters
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {} #create dictionary
        for i in s:
            if i not in dic:
                dic[i] = 1 #add 1 to the specific char element of the dictionary
            else:
                dic[i] += 1 #add 1 if we get the same char again
        
        for j in t:
            if j not in dic: #if j isn't in the dictionary, return false
                return False
            else:
                dic[j] -= 1 #take one away so that we don't run into a problem w the # of characters
        
        for val in dic.values(): #if a character value is left, it is not an anagram
            if val != 0:
                return False
        
        return True

#testing
s = "aaaaa"
t = "aaa"
print(isAnagram(s,t))
