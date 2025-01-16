class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        cur_total = max_total = sum(nums[:k])

        for i in range(k, len(nums)):
            
            cur_total += (nums[i]-nums[i-k])
            max_total = max(cur_total, max_total)

        return float(max_total)/k