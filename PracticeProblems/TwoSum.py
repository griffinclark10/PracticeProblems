#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#assuming the largest numbsers 

class Solution(object):
    def twoSum(self, nums, target):
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if (nums[a]+nums[b])==target:
                    return [a,b]


#find a way to make it not O(n^2)

class OnSolution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]