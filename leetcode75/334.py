import heapq

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        순회하면서 어떤 redundant한 정보를 저장할 것인가?

        - 이전의 등장했던 숫자 중, 
        """
        
        max_heap = []
        min_heap = []


