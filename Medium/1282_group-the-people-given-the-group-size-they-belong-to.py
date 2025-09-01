# Problem 1282: Group the People Given the Group Size They Belong To
# Difficulty: Medium
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        ans = []
        for size, people in count.items():
            while people:
                ans.append(people[:size])
                people = people[size:]
        return ans