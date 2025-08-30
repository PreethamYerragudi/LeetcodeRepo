# Problem 362: Design Hit Counter
# Difficulty: Medium
class HitCounter:

    def __init__(self):
        self.hits = {0 : 0}

    def hit(self, timestamp : int) -> None:
        self.hits[timestamp] = self.hits.get(timestamp, 0) + 1

    def getHits(self, timestamp : int) -> int:
        ans = 0
        for i in range(timestamp, timestamp - 300, -1):
            ans += self.hits.get(i, 0)
        return ans