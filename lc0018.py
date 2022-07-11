# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def __init__(self):
        self.output = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        self.backtrack(nums, 4, target, [], 0)
        return self.output

    def backtrack(self, nums, k, target, path, start):
        if k == 2:
            left = start
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    self.output.append(path + [nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while right > left > start and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right < len(nums) and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                    while right > left > start and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right < len(nums) and nums[right] == nums[right + 1]:
                        right -= 1
        else:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] * k > target or nums[-1] * k < target:
                    break
                self.backtrack(nums, k - 1, target - nums[i], path + [nums[i]], i + 1)
# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    result = Solution().fourSum(nums, target)
    print(result)
