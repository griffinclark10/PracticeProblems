def checkListForSame(list1, list2):
    maxList = max(list1, list2)
    minList = min(list1, list2)
    d = {}
    returnList = []
    for i in maxList:
        d[i] = 0
    for j in minList:
        if j in d:
            d[j] = 1
    for k in d:
        if d[k] == 1:
            returnList.append(k)
    return returnList


