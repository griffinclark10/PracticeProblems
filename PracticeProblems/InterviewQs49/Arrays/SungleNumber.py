def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return sum(nums)
        nums.sort()
        print(nums)
        if nums[0] != nums[1]: return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i+1] and nums[i-1] != nums[i]: return nums[i]
        return nums[len(nums)-1]

#testing
test = [4,1,5,1,5, 2, 3, 2, 3, 6, 8, 8, 6,9 ,4, 9, 10]
print(singleNumber(test))