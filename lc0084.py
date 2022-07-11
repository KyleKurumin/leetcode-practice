from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        result = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                h = heights[idx]
                w = i - stack[-1] - 1
                result = max(result, h * w)

            stack.append(i)
        return result