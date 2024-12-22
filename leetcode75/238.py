class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        루프를 돌면서 곱하기를 한번씩 하면 O(N^2)이기 때문에,
        해당 방법은 정답이 아니다.

        
        """
        answer = [1] * len(nums)

        for i, num in enumerate(nums):
            pass
