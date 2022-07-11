# coding=utf-8

from typing import List


# @solution-sync:begin
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                pos = mid + 1
                left = mid + 1
            else:
                pos = mid
                right = mid - 1
        return pos


# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5

    result = Solution().searchInsert(nums, target)
    print(result)
