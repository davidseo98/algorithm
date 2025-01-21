class Solution(object):

    # Beats 100% (runtime)
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        stack = [0]
        visited = set()
        visited.add(0)

        while stack:

            cur_room = stack.pop()
            next_rooms = rooms[cur_room]

            for next_room in next_rooms:
                if next_room not in visited:
                    stack.append(next_room)
                    visited.add(next_room)

        return len(rooms) == len(visited)