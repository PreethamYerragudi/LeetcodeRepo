# Problem 849: Maximize Distance to Closest Person
# Difficulty: Medium
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_id = -1
        prev_id = -1
        ans = 0

        for index, seat in enumerate(seats):
            if seat == 0:
                continue
            if prev_id == -1:
                first_id = index
                prev_id = index
            else:
                ans = max(ans, index - prev_id)
                prev_id = index

        ans = ans // 2

        if not seats[len(seats) - 1]:
            ans = max(ans, len(seats) - 1 - prev_id)
        if not seats[0]:
            ans = max(ans, first_id)
        return ans