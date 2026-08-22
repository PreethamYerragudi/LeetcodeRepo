# Problem 4024: Nearest Available Drone
# Difficulty: Easy
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        def dist(x, y):
            return abs(x - target[0]) + abs(y - target[1])
        ans = -1
        min_dist = float('inf')
        for i, v in enumerate(drones):
            x, y, r = v
            d = dist(x, y)
            if d <= r:
                if d < min_dist:
                    ans = i
                    min_dist = d
        return ans