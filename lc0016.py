# coding=utf-8

from typing import List


# @solution-sync:begin
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        result = -1 << 31

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current == target:
                    return current
                result = min(result, current, key=lambda x: abs(x - target))

                if current <= target:
                    left += 1
                else:
                    right -= 1
        return result


# @solution-sync:end


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1

    result = Solution().threeSumClosest(nums, target)
    print(result)
