# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
# @solution-sync:end


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = Solution().maxArea(height)
    print(result)