def intervalIntersection(listInput1, listInput2):
    finalList = []
    len1, len2 = len(listInput1), len(listInput2)
    twolist1 = []
    twolist2 = []
    for ele in listInput1:
        twolist1.append(range(ele[0], ele[1]+1))
    for ele in listInput2:
        twolist2.append(range(ele[0], ele[1]+1))
    onelist1 = [item for sublist in twolist1 for item in sublist]
    onelist2 = [item for sublist in twolist2 for item in sublist]
    print("list 1: ", onelist1, "\nList2: ", onelist2)
    sameList = checkListForSame(onelist1, onelist2)
    print(sameList)
    appendList = []
    for i in range(len(sameList)-1):
        print(sameList[i], "\n")
        if i == 0:
            appendList.append(sameList[i])
        if sameList[i]+1 != sameList[i+1]:
            print(sameList[i], "\n")
            appendList.append(sameList[i])
            finalList.append(appendList)
            appendList = [sameList[i+1]]    
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
#print(checkListForSame(l1,l2))
print(intervalIntersection(firstList, secondList))


class Solution:
    def intervalIntersection(self, A, B):
        ans, i, j = [], 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
        return ans