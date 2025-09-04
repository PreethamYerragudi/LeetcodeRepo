# Problem 3516: Find Closest Person
# Difficulty: Easy
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_dist = abs(x-z)
        y_dist = abs(y-z)

        if x_dist == y_dist:
            return 0
        elif x_dist < y_dist:
            return 1
        return 2