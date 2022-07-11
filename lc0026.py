# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        p = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[p - 1]:
                continue
            nums[p] = nums[i]
            p += 1
        return p
# @solution-sync:end


if __name__ == '__main__':
    nums = [1, 1, 2]

    result = Solution().removeDuplicates(nums)
    print(result)