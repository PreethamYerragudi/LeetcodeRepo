# Problem 1732: Find the Highest Altitude
# Difficulty: Easy
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [gain[0]]
        for i in range(1, len(gain)):
            arr.append(arr[i -1] + gain[i])
        return max(max(arr), 0)