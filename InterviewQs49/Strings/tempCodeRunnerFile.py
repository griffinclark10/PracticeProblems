"""
    :type s: str
    :rtype: int
    """
    newStr = ''
    negative = False
    s = s.replace(" ", "")
    s = s.replace("+", "")
    print(s)
    if s[0].isalpha(): return 0
    # if s[0] == "-": 
    #         negative = True
    #         s = s.replace("-", "")
    # for i in s:
    #     if s[i].isalpha():
    #         break
    #     newStr += i     
    # int(newStr)
    # if negative: newStr*=-1
    # return newStr