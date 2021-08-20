#taken from the comments section of leetcode:

def longestCommonPrefix(self, strs) -> str: #returns a string
        lcp = "" #in case none match
        for row in zip(*strs): #join each string in strs by their characters
            if all(i == row[0] for i in row): #if all of the characters in the first column are equal to the first row
                lcp += row[0] #add the character tot he lcp
            else:
                return lcp
        return lcp
           