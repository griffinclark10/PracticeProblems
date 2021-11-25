def intervalIntersection(listInput1, listInput2):
    finalList = []
    len1, len2 = len(listInput1), len(listInput2)
    list1 = []
    list2 = []
    for ele in len(len1):
        list1.append(range(ele[0], ele[1]))
    for ele in len(len2):
        list2.append(range(ele[0], ele[1]))
    sameList = checkListForSame(list1, list2)
    for i in sameList:
        pass        




    return finalList

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


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]


l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
l2 = [1,5,6,7,9,13]
print(checkListForSame(l1,l2))