from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            while left < right and nums[left] == nums[left + 1]:
                left += 1

            if left == right:
                break

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return True if nums[left] == target else False
    