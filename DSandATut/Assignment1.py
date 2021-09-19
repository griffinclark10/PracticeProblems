test1 = {
    'input': {
        'nums': [5, 6, 8, 0, 2, 3]
        },
    'output' : 3
}

test2 = {
    'input': {
        'nums': [49, 56, 65, 234, -5, 21, 33]
        },
    'output' : 4
}

test3 = {
    'input': {
        'nums': [1,2,3,4,5]
        },
    'output' : 0
}

test4 = {
    'input': {
        'nums': []
        },
    'output' : 0
}



def binarySearch(numArr):
    lo = 0
    hi = len(numArr)-1
    if lo == hi: return 0

    while lo <= hi:
        mid = (lo + hi) //2
        mid_number = numArr[mid]
        print('lo: ', lo, ', hi: ', hi, ', mid: ', mid)
        if mid > 0 and mid_number < numArr[mid-1]:
            return mid
        elif mid_number > numArr[hi]:
            lo = mid+1
        elif mid_number < numArr[hi]:
            hi = mid-1
    return 0


def shiftCount(numArr, search):
    return search(numArr)


print(test4['output'] ==  shiftCount(test4['input']['nums'], binarySearch))