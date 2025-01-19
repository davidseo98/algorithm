from collections import deque

class Solution(object):

    # Beats 46.49% (runtime)
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        dxs = [1, -1, 0, 0]
        dys = [0, 0, 1, -1]

        row_cnt, col_cnt = len(maze), len(maze[0])
        en_x, en_y = entrance
        visited = [[False] * col_cnt for _ in range(row_cnt)]
        visited[en_x][en_y] = True

        queue = deque([(en_x, en_y, 0)])

        while queue:

            cur_x, cur_y, cur_cnt = queue.popleft()
            if (cur_x in [0, row_cnt-1] or cur_y in [0, col_cnt-1])\
                and not (cur_x==en_x and cur_y==en_y):
                return cur_cnt
            
            for dx, dy in zip(dxs, dys):
                next_x, next_y = cur_x+dx, cur_y+dy

                if 0 <= next_x < row_cnt \
                    and 0 <= next_y < col_cnt \
                    and maze[next_x][next_y] == "." \
                    and not visited[next_x][next_y]:

                    queue.append((next_x, next_y, cur_cnt+1))
                    visited[next_x][next_y] = True
                    
        return -1
