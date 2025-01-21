from collections import deque

class Solution(object):

    # Beats 58.02 (runtime)
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        cols = len(grid[0])
        rows = len(grid)
        
        dxs = [0, 0, 1, -1]
        dys = [1, -1, 0, 0]

        queue = deque([])
        cur_min = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y, cur_min))

        while queue:

            cur_x, cur_y, cur_min = queue.popleft()

            for dx, dy in zip(dxs, dys):
                next_x, next_y = cur_x+dx, cur_y+dy

                if 0 <= next_x < rows \
                    and 0 <= next_y < cols \
                    and grid[next_x][next_y] == 1:

                    queue.append((next_x, next_y, cur_min+1))
                    grid[next_x][next_y] = 2

        for row in grid:
            for tomato in row:
                if tomato == 1:
                    return -1
                
        return cur_min