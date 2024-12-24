import heapq

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        순회하면서 어떤 redundant한 정보를 저장할 것인가?

        - 이전의 등장했던 숫자 중에서 현재 숫자는 몇등인가? -> 현재 숫자보다 작은 숫자의 개수 파악
        - Binary search를 사용해서 현재까지 나온 숫자 중에서 몇등인지 파악?
        """
        
        max_heap = []
        min_heap = []


