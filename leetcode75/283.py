class Solution(object):
    
    # naive solution, beats 25.77% runtime
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        index = 0
        end = len(nums)-1

        while index < len(nums) and index <= end:
            num = nums[index]
            if num == 0:
                nums.append(nums.pop(index))
                end -= 1
            else :
                index += 1
        