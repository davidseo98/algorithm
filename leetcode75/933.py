from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque([])

    # Beats 8.62%(runtime)
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.queue.appendleft(t)

        cnt = 0

        for req in self.queue:

            if t-3000 <= req <= t:
                cnt += 1
            else:
                return cnt
    
    # Beats 95.22% (runtime)
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.queue.appendleft(t)

        while self.queue[-1] < t-3000:
            self.queue.pop()

        return len(self.queue)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)