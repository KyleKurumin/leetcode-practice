from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for start, end in intervals:
            if not newInterval or end < newInterval[0]:
                ans.append([start, end])
            elif start <= newInterval[-1]:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            else:
                ans.append(newInterval)
                ans.append([start, end])
                newInterval = None
        if newInterval:
            ans.append(newInterval)
        return ans
    