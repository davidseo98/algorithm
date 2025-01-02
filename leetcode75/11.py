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
        
        s, e = 0, 1

        max_area = min(height[0], height[1])

        while e < len(height)-1:

            start_move_area = None if e-s==1 else (e-s-1) * min(height[s+1], height[e])
            end_move_area = (e+1-s) * min(height[s], height[e+1])

            if start_move_area == None or start_move_area < end_move_area:
                e += 1
                max_area = max(max_area, end_move_area)

            else:
                s += 1
                max_area = max(max_area, start_move_area)

        return max_area
    
    # 32/63 case passed
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        s, e = 0, len(height)-1
        left_idx, right_idx = s, e
        
        while s < e:
            
            if s+1 < e and s+1 - left_idx < height[s+1] - height[left_idx]:
                s += 1
            
            elif e-1 > s and right_idx - e-1 < height[e-1] - height[right_idx]:
                e -= 1

            else:
                s -= 1
                e -= 1

        return (right_idx-left_idx) * min(height[right_idx], height[left_idx])
