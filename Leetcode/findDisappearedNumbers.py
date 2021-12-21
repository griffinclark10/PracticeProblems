def findDisappearedNumbers(nums):
    d = {}
    for i in range(1, len(nums)+1):
        d[i] = 0
    for i in nums:
        d[i] = 1
        print(d)
    return [a for a in d if d[a] == 0]

nums = [4,3,2,7,8,2,3,1]
nums1 = [1,1]
print(findDisappearedNumbers(nums1))