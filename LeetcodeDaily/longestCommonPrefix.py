def longestCommonPrefix(strs):
    # first = words[0]
    # start = first[0]
    # prefix = ""
    # for j in range(len(first)):
    #     prefix += first[j]
    #     for i in range(1, len(words)):
    #         print(words[i])
    #         if words[i].startswith(start) != True:
    #             return ""
            
    # return prefix    
    strs.sort()
    prefix = strs[0]
    while prefix != strs[-1][:len(prefix)]:
        prefix = prefix[:-1]
    return prefix    

words = ["flower","flow","flight"]
a = longestCommonPrefix(words)
print(a)