#rotate the array by k spaces

def rotate1(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newArr = [0] * (len(nums))
        for i, number in enumerate(nums):
            a = i + k
            if len(nums) <= i+k:
                a = i+k - len(nums)
            newArr[a] = number
        return newArr

#better solution
def rotate2(nums, k):
        k = k % len(nums) #gives 2, this is assuring that our k is smaller than our list
        # index of -k (-2) is the second last value in the list, so the new list will go from the second last value to
        #the last, and then go from the first value to the second last, replacing the list by using nums[:]
        nums[:] = nums[-k:] + nums[:-k] 
        return nums

#another solution
from collections import deque

def rotate3(self, nums, k):
    d = deque(nums) #created double ended queue which has the option to rotate
    d.rotate(k)
    nums[:] = list(d) #make it a list again

#testing
tester = [1,2,3,4,5,6,7]
print(rotate2(tester, 2))

