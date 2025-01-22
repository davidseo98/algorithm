from collections import defaultdict

class Solution(object):

    # Beats 25.31(runtime)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        graph = defaultdict(list)

        row_cnt, col_cnt = len(isConnected), len(isConnected[0])

        for x in range(row_cnt):
            for y in range(col_cnt):
                if x != y and isConnected[x][y]:
                    graph[x].append(y)
                    graph[y].append(x)

        visited = set()
        province_cnt = 0

        for node in graph.keys():

            if node in visited: continue

            province_cnt += 1
            stack = [node]

            while stack:
                cur_node = stack.pop()
                for next_node in graph[cur_node]:
                    if next_node not in visited:
                        stack.append(next_node)
                        visited.add(next_node)

        return province_cnt
