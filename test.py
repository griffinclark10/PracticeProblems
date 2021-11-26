firstList = [[0,2],[5,10],[13,23],[24,25]]
secList = []

for ele in firstList:
    print(range(ele[0], ele[1]))
    secList.append(range(ele[0], ele[1]+1))
        
print(secList)
