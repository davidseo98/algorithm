import heapq

class Solution(object):

    # Beats 47.15% (runtime)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            answer = heapq.heappop(nums)

        return -answer
        