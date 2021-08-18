#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

#this shit is so god damn hard wtf, not the working answer, i will be skipping it
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    bigger = max(nums1, nums2)
    smaller = min(nums1, nums2)
    #print(smaller)
    revSmaller = smaller.reverse()
    for i in range(len(bigger) - len(smaller)):
        pass


#testing
test1 = [1,2,3,4]
test2 = [1,2]
print(intersect(test1, test2))