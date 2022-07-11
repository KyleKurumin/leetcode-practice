# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return left if nums[left] == target else - 1
# @solution-sync:end


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    result = Solution().search(nums, target)
    print(result)
