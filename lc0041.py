# coding=utf-8

from typing import List


# @solution-sync:begin
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 2, 0]

    result = Solution().firstMissingPositive(nums)
    print(result)
