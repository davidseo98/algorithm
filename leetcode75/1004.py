class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        start, end = 0, 1
        length = len(nums)

        while True:

            if end < length - 1 and (nums[end + 1]==1 or k > 0):
                if nums[end + 1]==0:
                    k -= 1
                end += 1
            else:

                if nums[start]==0:
                    k+= 1
                start += 1
            




