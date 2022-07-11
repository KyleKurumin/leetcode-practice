from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step, end, farthest = 0, 0, 0
        for i in range(len(nums[:-1])):
            farthest = max(farthest, i + nums[i])
            if i == end:
                step += 1
                end = farthest
        return step