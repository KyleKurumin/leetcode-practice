from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        previous = intervals[0]
        output = []

        for i in range(1, len(intervals)):
            current = intervals[i]
            start, end = current
            if start <= previous[1]:
                previous = [min(previous[0], start), max(previous[1], end)]
            else:
                output.append(previous)
                previous = current
        output.append(previous)
        return output
