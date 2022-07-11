# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] == val:
                continue

            nums[slow] = nums[fast]
            slow += 1

        return slow
# @solution-sync:end


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3

    result = Solution().removeElement(nums, val)
    print(result)