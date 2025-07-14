from collections import deque


class Solution(object):

    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        q = deque()
        q.appendleft((0, 0))
        seen = set()
        seen.add((0, 0))
        while q:
            curr = q.pop()
            a, b = curr
            print(curr)
            if a + b == target:
                return True
            next_states = [(x, b), (a, y), (0, b), (a, 0),
                           (a - min(a, y - b), b + min(a, y - b)),
                           (a + min(b, x - a), b - min(b, x - a))]
            for state in next_states:
                if state not in seen:
                    seen.add(state)
                    q.append(state)
        return False
