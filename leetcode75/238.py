class Solution(object):

    # Beats 13.02% (runtime)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        루프를 돌면서 곱하기를 한번씩 하면 O(N^2)이기 때문에,
        해당 방법은 정답이 아니다.        
        """
        prefix = []
        suffix = []
        length = len(nums)

        cur = nums[0]
        for i in range(length):

            if i != 0:
                cur *= nums[i]

            prefix.append(cur)

        cur = nums[length-1]
        for i in range(length - 1, -1, -1):
            
            if i != length-1:
                cur *= nums[i]
            
            suffix.append(cur)

        suffix = suffix[::-1]

        answer = []

        for i in range(length):

            pre = 1 if i == 0 else prefix[i-1]
            suf = 1 if i == length - 1 else suffix[i+1]

            answer.append(pre * suf)

        return answer
    
    # Beats 22.70% (runtime)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        루프를 돌면서 곱하기를 한번씩 하면 O(N^2)이기 때문에,
        해당 방법은 정답이 아니다.        
        """
        prefix = nums[:]
        suffix = nums[:]
        length = len(nums)

        for i in range(1, length):
            prefix[i] *= prefix[i-1]

        for i in range(length - 2, -1, -1):
            suffix[i] *= suffix[i+1]

        answer = []

        for i in range(length):

            pre = 1 if i == 0 else prefix[i-1]
            suf = 1 if i == length - 1 else suffix[i+1]

            answer.append(pre * suf)

        return answer
    
    # Beats 25.02% (runtime)
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        루프를 돌면서 곱하기를 한번씩 하면 O(N^2)이기 때문에,
        해당 방법은 정답이 아니다.        
        """
        length = len(nums)
        prefix = [1] + nums + [1]
        suffix = [1] + nums + [1]

        for i in range(1, length+1):
            prefix[i] *= prefix[i-1]
            suffix[length-i+1] *= suffix[length-i+2]

        answer = []

        for i in range(1, length+1):
            answer.append(prefix[i-1]*suffix[i+1])

        return answer



