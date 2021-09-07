def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for val in nums:
                if val == 0:
                        nums.remove(0)
                        nums.append(0)
        return nums


#testing
test = [0]
print(moveZeroes(test))

