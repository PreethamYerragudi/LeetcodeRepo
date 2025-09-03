# Problem 759: Employee Free Time
# Difficulty: Hard
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        lst = []

        for intervals in schedule:
            for interval in intervals:
                lst.append((interval.start, interval.end))
        lst.sort()
        
        num = []
        beg, end = -1, -1

        for start, finish in lst:
            if beg == -1:
                beg = start
                end = finish
            elif start <= end:
                end = max(end, finish)
            else:
                num.append(Interval(end, start))
                beg = start
                end = finish
        return num