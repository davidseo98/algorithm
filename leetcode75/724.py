class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = sum(nums)

        for idx in range(len(nums)):

            cur = nums[idx]
            right -= cur

            if left == right:
                return idx

            left += cur
        
        return -1
        