from collections import defaultdict

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        element_by_row = defaultdict(set)
        element_by_col = defaultdict(set)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                
                val = grid[x][y]

                element_by_col[y].add((val, x))
                element_by_row[x].add((val, y))

        answer = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if element_by_row[x] == element_by_col[y]:
                    answer += 1

        return answer
