from collections import defaultdict

class Solution(object):

    # beats 100% (runtime)
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        cnt = defaultdict(int)
        for num in arr:
            cnt[num] += 1

        values = cnt.values()
        return len(values) == len(set(values))