def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        print(nums)
        for i in range(1, 1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

#testing
test = [1,2,3,1]
print(containsDuplicate(test))