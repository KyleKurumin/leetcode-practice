from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return self.bin_search(matrix[i], target)

    def bin_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return False
