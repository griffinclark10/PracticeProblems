#given a list of sorted numbers, remove the duplicates

def removeDuplicates(nums):
    k =0
    pops = []
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            pops.append(i)
            k +=1
    l = 0
    for j in pops:
        nums.pop(j-l)
        l +=1
    return k, nums

a = [1,1,2, 3, 5, 6, 6, 6, 7, 9, 9, 10, 22, 22, 22, 22, 24, 28, 30, 30]
print(removeDuplicates(a))
            