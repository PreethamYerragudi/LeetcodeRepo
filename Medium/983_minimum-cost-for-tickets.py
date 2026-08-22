# Problem 983: Minimum Cost For Tickets
# Difficulty: Medium
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        target = max(days)
        def findLastDayReached(day):
            l, r = 0, len(days) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                d = days[m]
                if d < day:
                    ans = m
                    l = m + 1
                else:
                    r = m - 1
            return ans
        @lru_cache(maxsize=None)
        def solve(i):
            if i >= len(days):
                return 0
            return min(
                costs[0] + solve(findLastDayReached(days[i] + 1) + 1),
                costs[1] + solve(findLastDayReached(days[i] + 7) + 1),
                costs[2] + solve(findLastDayReached(days[i] + 30) + 1)
            )

        return solve(0)