# Problem 4025: Minimize the Maximum Waiting Time at Synchronized Traffic Lights
# Difficulty: Medium
class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        r = [arrivalTime[i] % period for i in range(len(arrivalTime))]
        m = max(lights)
        ans = period
        for v in r:
            if v >= m:
                ans = min(ans, v)
        return period - ans