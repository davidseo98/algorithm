from itertools import combinations

class Solution(object):

    # naive approach time exceeded (53/63 passed)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        combs = combinations(range(len(height)), 2)

        answer = -1
        for comb in combs:
            s, e = comb
            w = e - s
            area = min(height[s], height[e]) * w

            if area > answer:
                answer = area

        return answer
    
    """
    Case
    height = [1, 1, 1, 10, 10, 1, 1, 1]
    
    어떤 규칙에 의해서 start, end를 업데이트 할 것인가?

    Greedy approach
    
    1. start에서 오른쪽에 있는 기둥을 순차적으로 scan
        -> 이동 후보지 조건 : 기둥까지 거리 차이보다 높이 차이가 더 많이 난다 (end 기둥의 높이를 초과하는 길이는 무시된다)
        -> 후보지 중에서 가장 차이 값이 큰 곳으로 이동

    2. end도 왼쪽으로 순차적으로 scan하면서 동일한 과정
        * start와 동일한 값은 안된다.
    """
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        s, e = 0, len(height) - 1

        cur = min(height[e], height[s]) * (e - s)
        while s < e:

            temp_s = s

