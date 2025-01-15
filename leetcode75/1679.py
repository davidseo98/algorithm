from collections import defaultdict

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
    
    # Beats 82.26% (runtime)
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt_dict = defaultdict(int)
        answer = 0

        for num in nums:
            cnt_dict[num] += 1
        
        for key in cnt_dict.keys():
            cur, remain = cnt_dict[key], cnt_dict[k-key]
            if cur and remain:
                increment = min(cur, remain) if key != k-key else cur//2
                cnt_dict[key] -= increment
                cnt_dict[k-key] -= increment
                answer += increment
        
        return answer

