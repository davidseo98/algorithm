class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        cur = 0
        temp = 0
        for g in gain:
            temp += g
            cur = max(cur, temp)

        return cur