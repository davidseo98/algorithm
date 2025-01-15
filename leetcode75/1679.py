class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()

        s, e = 0, len(nums)-1
        cnt = 0 

        while s < e:

            cur_sum = nums[s] + nums[e]

            if cur_sum == k:
                s += 1
                e -= 1
                cnt += 1
            
            elif cur_sum > k:
                e -= 1
            else:
                s += 1
        
        return cnt

