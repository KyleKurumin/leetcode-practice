from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                pre = height[stack.pop()]

                if not stack:
                    break

                min_height = min(height[i], height[stack[-1]]) - pre
                ans += min_height * (i - stack[-1] - 1)

            stack.append(i)
        return ans