# Problem 767: Reorganize String
# Difficulty: Medium
import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)
        ans = []
        prev_char = None
        while heap:
            value, char = heappop(heap)
            if heap:
                value2, char2 = heappop(heap)
                ans.append(char)
                ans.append(char2)
                if value + 1 != 0:
                    heappush(heap, (value + 1, char))
                if value2 + 1 != 0:
                    heappush(heap, (value2 + 1, char2))
            else:
                if value < -1:
                    return ""
                ans.append(char)
        return "".join(ans)
