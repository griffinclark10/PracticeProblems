#create an ATOI function (like the ones in C/C++) 

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    newStr = ''
    negative = False
    s = s.replace(" ", "")
    s = s.replace("+", "")
    if s[0].isalpha(): return 0
    if s[0] == "-": 
            negative = True
            s = s.replace("-", "")
    #print(s)
    for i in range(len(s)):
        #print(i)
        if s[i].isalpha() or s[i] == ".":
            break
        newStr += s[i]     
    newStr = int(newStr)
    if negative: newStr*=-1
    if newStr > 2**31 - 1: newStr = 2**31 - 1
    if newStr < -2**31: newStr = -2**31
    return newStr
    #doesn't work with test case s = +-120 (should return 0)

    #found in discussion:
def myAtoi2(s):
    if len(s) == 0 : return 0
    ls = list(s.strip())

    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+'] : del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit() :
        ret = ret*10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))
    #still get an error here so imma skip this
        


#testing
s = "3.14159"
#myAtoi(s)
print(myAtoi(s))