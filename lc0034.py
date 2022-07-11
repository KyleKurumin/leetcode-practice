# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        rb = left
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                rb = mid
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        lb = left
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1

        if nums[lb] == target:
            return [lb, rb]
        else:
            return [-1, -1]
# @solution-sync:end


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    result = Solution().searchRange(nums, target)
    print(result)
