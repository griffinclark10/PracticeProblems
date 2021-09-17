# given an array of integers in ascending order and a number, find the starting and ending position of that given number
#return the idecies

def binary_search(lo, hi, condition): 
    while lo <= hi:
        mid = (lo + hi)//2
        result = condition(mid)
        if result == "found": return mid
        elif result == "left": hi = mid - 1
        else: lo = mid+1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return 'right'
        else: 
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return 'right'
        else: 
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last(nums, target):
    return first_position(nums, target), last_position(nums, target)

nums = [5,7,7, 8,8,10]
target = 8

print(first_and_last(nums, target))