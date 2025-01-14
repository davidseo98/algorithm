import heapq
import itertools

class Solution(object):

    """
        :type nums: List[int]
        :rtype: bool
    """
    """
    순회하면서 어떤 redundant한 정보를 저장할 것인가?
    - 이전의 등장했던 숫자 중에서 현재 숫자는 몇등인가? -> 현재 숫자보다 작은 숫자의 개수 파악
    - Binary search를 사용해서 현재까지 나온 숫자 중에서 몇등인지 파악?
    - 이전에 등장한 숫자 중에서 등수를 알아도 정답을 알 수 없다.
        예를 들어 현재 숫자보다 작은 숫자가 2개 있었다고 해도, 등장 순서에 따라 계속 상승 했는지 안했는지 달라지기 때문이다.
        예) 2, 1, 5 -> 증가 배열의 길이가 2이다.
    
    - 현재 숫자보다 작은 숫자 중에, 가장 가까운 숫자를 찾고, 해당 숫자의 최대 증가 배열 길이 + 1
        예) 2, 1, 5, 0, 4, 6 (한 개씩 순회)
            2 -> 2는 과거 등장한 숫자가 없기 때문에 최대 증가 배열 길이 = 0
            1 -> 1은 과거 등장한 숫자 중 본인보다 작은 숫자가 없기 때문에 최대 증가 배열 길이 = 0
        이 방법도 오답.
        현재 숫자와 가장 가까운 숫자를 찾는 것이 아니라, 과거에 등장했던 숫자 중에 본인보다 작고, 최대 증가 배열의 길이가 가장 길었던 숫자를 찾아야 함
    
    - 배열을 순회하면서, 지금까지 순회했던 숫자들을 포함해서 최대 증가 배열의 길이가 얼마인지 기록해야 한다.
        예) 2, 1, 5, 0, 4, 6
            2 -> 2 : 1 (본인까지 포함)
            1 -> 1 : 1
            5 -> 5 : 2
            0 -> 0 : 1
            4 -> 4 : 2
            6 -> 6 : 3 
    """
    
    # Naive solution (Failed - time exceed, 32/84 test cases)
    def increasingTriplet(self, nums):
        indices = list(range(len(nums)))

        combs = itertools.combinations(indices, 3)

        for comb in combs:

            i1, i2, i3 = comb
            if nums[i1] < nums[i2] < nums[i3]:
                return True
        
        return False

    # (Failed - wrong answer, 71/84 test cases)
    def increasingTriplet(self, nums):

        lists = []

        for num in nums:
            
            add_flag = False
            for l in lists:
                if l[-1] < num:
                    l.append(num)
                    add_flag = True

            if add_flag == False:
                lists.append([num])

        max_len = max([len(l) for l in lists])

        if max_len >= 3: return True
        return False 
    
    def increasingTriplet(self, nums):

        first, second = float("inf")

        for num in nums:

            if num >= first:
                first = num
            elif num >= second:
                second = num
            else: return True

        return False
