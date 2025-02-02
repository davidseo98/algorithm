class Solution(object):

    def __init__(self):
        self.memo = [-1] * 38
        self.memo[0] = 0
        self.memo[1] = 1
        self.memo[2] = 1

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if self.memo[n] == -1:
            self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.memo[n]