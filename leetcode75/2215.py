class Solution(object):

    # Beats 52% (runtime)
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        num1_set = set(nums1)
        num2_set = set(nums2)
        left = num1_set.difference(num2_set)
        right = num2_set.difference(num1_set)

        return [list(left), list(right)]
