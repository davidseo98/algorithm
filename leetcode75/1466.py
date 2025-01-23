from collections import defaultdict

class Solution(object):

    """
    Reverse the problem:
    How many roads do we have to reorder to be able to visit
    every node starting from O?
    And then, do n - 1 - cnt
    """

    # Beats 75.8% (runtime)
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        out_graph = defaultdict(list)
        in_graph = defaultdict(list)
        forward_reorder_cnt = 0

        for start, end in connections:
            out_graph[start].append(end)
            in_graph[end].append(start)

        stack = [0]
        visited = {0}

        while stack:

            cur_node = stack.pop()

            for out_node in out_graph[cur_node]:
                if out_node not in visited:
                    stack.append(out_node)
                    visited.add(out_node)
            for in_node in in_graph[cur_node]:
                if in_node not in visited:
                    stack.append(in_node)
                    visited.add(in_node)
                    forward_reorder_cnt += 1

        return n - 1 - forward_reorder_cnt
                
        