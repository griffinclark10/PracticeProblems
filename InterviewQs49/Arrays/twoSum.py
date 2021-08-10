#find which values in an array add up to a target and return their indices
#must be in less than O(n^2)
#exactly 1 solution and same element can't be used twice

""" def twoSum(nums, target):
    options = []
    for i in range(target):
        if target-i in nums:
            if i in nums:
                print(i)
                if target-i == i:
                    options.append(i)
                options.append(i)
    print(options)
    
    index = []
    for j, vals in enumerate(options):
        if target-vals in nums and target-vals != options[j]:
            index.append(nums.index(vals))
    return sorted(index) """
#above is what I tried, it didn't work :/

def twoSum(nums, target):
    d = {}
    print(d)
    for i, n in enumerate(nums):
        m = target - n #m is the target minus the value
        if m in d: #if m in in the dictionary aleady
            return [d[m], i]
        else: #if not, add to the dictionary
            d[n] = i #the value n has the indix i

#testing
testNums = [3,2,3]
testTarget = 6
print(twoSum(testNums, testTarget))