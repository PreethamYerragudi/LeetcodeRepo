# Problem 1419: Minimum Number of Frogs Croaking
# Difficulty: Medium
from collections import Counter
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        num_available = 0
        num_needed = 0
        count = Counter("croak")
        for char in croakOfFrogs:
            if char == 'c':
                if num_available:
                    num_available -= 1
                else:
                    num_needed += 1
            if char == 'k':
                num_available += 1
            count[char] += 1
            if count['r'] > count['c'] or count['o'] > count['r'] or count['a'] > count['o'] or count['k'] > count['a']:
                return -1
        for i in range(len(count.values()) - 1):
            if list(count.values())[i] != list(count.values())[i + 1]:
                return -1
        return num_needed
